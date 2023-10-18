import ast
import regex
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from llm_miner.text.prompt import PROMPT_TYPE, PROMPT_EXT, FT_TYPE, FT_HUMAN
from llm_miner.schema import Paragraph
from llm_miner.format import Formatter
from llm_miner.error import StructuredFormatError, LangchainError, TokenLimitError
from llm_miner.pricing import TokenChecker, update_token_checker


class TextMiningAgent(Chain):
    type_chain: LLMChain
    extract_chain: LLMChain
    input_key: str = "element"
    output_key: str = "output"

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]
    
    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]
    
    def _write_log(self, text: str, run_manager):
        run_manager.on_text(f"\n[Property Mining] ", verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color="yellow")

    def _parse_output(self, output: str) -> Dict[str, str]:
        if regex.search(r"^\s*```JSON", output) and not regex.search(r"```\s*$", output):
            raise TokenLimitError('Output does not finished before token limits', output)
        
        output = output.replace("```JSON","")
        output = output.replace("```","")
        output = output.strip()
        if regex.search(r"[Ii] do not know", output):
            return [output]
        try:
            return ast.literal_eval(output)
        except Exception as e:
            raise StructuredFormatError(e, output)
    
    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()

        explanation = self._add_explanation()
        element: Paragraph = inputs[self.input_key]
        token_checker: TokenChecker = inputs.get('token_checker')
        paragraph: str = element.clean_text   # change content -> clean_text

        llm_kwargs = {
            'explanation': explanation,
            'paragraph': paragraph,
        }
        try:
            llm_output = self.type_chain.run(
                **llm_kwargs,
                callbacks=callbacks,
                stop=["Paragraph:"]
            )
        except Exception as e:
            element.add_intermediate_step('text-property-type', str(e))
            raise LangchainError(e)
        else:
            element.add_intermediate_step('text-property-type', llm_output)

        if token_checker:
            update_token_checker(
                name_step='text-property-type',
                chain=self.type_chain,
                token_checker=token_checker, 
                llm_kwargs=llm_kwargs, 
                llm_output=llm_output
            )

        property_type = self._parse_output(llm_output)
        self._write_log(str(property_type), _run_manager)
        element.set_include_properties(property_type)

        st_data_string = ""
        info_string = ""
        example_string = ""
        prop_string = ""

        for prop in property_type:
            try:
                st_data = Formatter.structured_data[prop]
                info = Formatter.information[prop]
                example = Formatter.example_text[prop]
            except KeyError:
                self._write_log(f"There are no format for {prop}", _run_manager)
                continue

            st_data_string += f"- {st_data}\n"
            info_string += f"- {info}\n"
            example_string += f"- {example}\n"
            prop_string += f"{prop}, "

        llm_kwargs={
            'prop': prop_string,
            'structured_data': st_data_string,
            'information': info_string,
            'example': example_string,
            'paragraph': paragraph,
        }
        try:
          llm_output = self.extract_chain.run(
              **llm_kwargs,
              callbacks=callbacks,
              stop=["Paragraph:"]
          )
        except Exception as e:
            element.add_intermediate_step('text-property-extract', str(e))
            raise LangchainError(e)
        else:
            element.add_intermediate_step('text-property-extract', llm_output)
            
        if token_checker:
            update_token_checker(
                name_step='text-property-extract',
                chain=self.extract_chain,
                token_checker=token_checker, 
                llm_kwargs=llm_kwargs, 
                llm_output=llm_output
            )

        st_output = self._parse_output(llm_output)
        self._write_log(f"{st_output}", _run_manager)

        element.set_data([st_output])
        return {"output": st_output}
    
    def _add_explanation(self,) -> str:
        erase_list = [
            "cell_volume",
            "conversion",
            "reaction_yield",
            "chemical_formula",
        ]
        formatter = Formatter
        target_items = list(formatter.explanation.keys())
        target_items = [item for item in target_items if item not in erase_list]
        explained_props = ""
        for item in target_items:
            explained_props += "\n" + f"- {item}: " + formatter.explanation[item].strip()
        return explained_props.strip()

    @classmethod
    def from_llm(
        cls,
        type_llm: BaseLanguageModel,
        extract_llm: BaseLanguageModel,
        *,
        prompt_type: str = PROMPT_TYPE,
        prompt_extract: str = PROMPT_EXT,
        ft_type: str = FT_TYPE,
        ft_human: str = FT_HUMAN,
        **kwargs,
    ) -> Chain:
        
        if type_llm.model_name.startswith('ft:'): # fine-tuned model
            system_prompt = SystemMessagePromptTemplate.from_template(ft_type)
            human_prompt = HumanMessagePromptTemplate.from_template(ft_human)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_prompt, human_prompt]
            )
            type_chain = LLMChain(
                llm=type_llm,
                prompt=chat_prompt,
            )
        else:
            template_type = PromptTemplate(
                template=prompt_type,
                input_variables=["explanation", "paragraph"],
            )
            type_chain = LLMChain(llm=type_llm, prompt=template_type)

        if extract_llm.model_name.startswith('ft:'): # fine-tuned model
            raise NotImplementedError('Fine-tuning model for extract is not implemented.')
        else:
            template_extract = PromptTemplate(
                template=prompt_extract,
                input_variables=["prop", "structured_data", "information", "example", "paragraph"],
            )
            extract_chain = LLMChain(llm=extract_llm, prompt=template_extract)

        return cls(
            type_chain=type_chain,
            extract_chain=extract_chain,
            **kwargs
        )
    
import ast
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
      ChatPromptTemplate,
      SystemMessagePromptTemplate,
      HumanMessagePromptTemplate,
)

from llm_miner.schema import Paragraph
from llm_miner.error import StructuredFormatError, TokenLimitError, LangchainError
from llm_miner.format import Formatter
from llm_miner.table.crystal.prompt import CRYSTAL_CATEGORIZE, CRYSTAL_EXTRACT, FT_TYPE, FT_HUMAN
from llm_miner.pricing import TokenChecker, update_token_checker


class CrystalTableAgent(Chain):
    categorize_chain: LLMChain
    extract_chain: LLMChain
    input_key: str = "element"
    output_key: str = "output"
    included_props: list = []

    @classmethod
    def from_llm(
        cls,
        type_llm: BaseLanguageModel,
        extract_llm: BaseLanguageModel,
        *,
        prompt_categorize: str = CRYSTAL_CATEGORIZE,
        prompt_extract: str = CRYSTAL_EXTRACT,
        ft_type: str = FT_TYPE,
        ft_human: str = FT_HUMAN,
        **kwargs,
    ) -> Chain:
        if type_llm.model_name.startswith('ft:'):
            system_prompt = SystemMessagePromptTemplate.from_template(ft_type)
            human_prompt = HumanMessagePromptTemplate.from_template(ft_human)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_prompt, human_prompt]
            )
            categorize_chain = LLMChain(llm=type_llm, prompt=chat_prompt)
        else:
            template_categorize = PromptTemplate(
                template=prompt_categorize,
                template_format="jinja2",
                input_variables=['paragraph'],
            )
            categorize_chain = LLMChain(llm=type_llm, prompt=template_categorize)

        template_extract = PromptTemplate(
            template=prompt_extract,
            template_format="jinja2",
            input_variables=['prop', 'format', 'paragraph'],
        )
        extract_chain = LLMChain(llm=extract_llm, prompt=template_extract)

        return cls(
            categorize_chain=categorize_chain,
            extract_chain=extract_chain,
            **kwargs
        )

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]

    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]

    def _write_log(self, text, run_manager):
        run_manager.on_text('\n[Included props] ', verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color='yellow')

    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()

        element: Paragraph = inputs[self.input_key]
        paragraph: str = element.clean_text
        token_checker: TokenChecker = inputs['token_checker']
        llm_kwargs={
            'paragraph': paragraph
        }
        try:
            included_props = self.categorize_chain.run(
                **llm_kwargs,
                callbacks=callbacks,
                # stop=["Input:"]
            )
        except Exception as e:
            element.add_intermediate_step('table-crystal-categorize', str(e))
            raise LangchainError(e)
        else:
            element.add_intermediate_step('table-crystal-categorize', included_props)

        if token_checker:
            update_token_checker(
                name_step='table-crystal-categorize',
                chain=self.categorize_chain,
                token_checker=token_checker,
                llm_kwargs=llm_kwargs,
                llm_output=included_props,
            )

        self.included_props = self._parse_output_props(included_props)

        for_print_props = [item.replace("_", " ") for item in self.included_props]
        self._write_log(str(for_print_props), _run_manager)

        props = self.included_props[:]
        if "chemical_formula" in props:
            props.remove("chemical_formula")

        if not props:
            return {"output": ["No properties found"]}

        format = self._make_format(props)

        llm_kwargs = {
            'prop': props,
            'format': format,
            'paragraph': paragraph,
        }
        try:
            output = self.extract_chain.run(
                **llm_kwargs,
                callbacks=callbacks,
                stop=["Input:"]
            )
        except Exception as e:
            element.add_intermediate_step('table-crystal-categorize', str(e))
            raise LangchainError(e)
        else:
            element.add_intermediate_step('table-crystal-categorize', output)

        if token_checker:
            update_token_checker(
                name_step='table-crystal-extract',
                chain=self.extract_chain,
                token_checker=token_checker,
                llm_kwargs=llm_kwargs,
                llm_output=output,
            )

        output = self._parse_output_json(output)
        # print("OUTPUT arrived: ", output)
        return {"output": output}

    def _parse_output_props(self, output: str) -> Dict[str, str]:
        output = output.replace("List:", "").strip()
        try:
            list_ = ast.literal_eval(output)
        except Exception as e:
            raise StructuredFormatError(e)
        else:
            return list_

    def _parse_output_json(self, output: str) -> Dict[str, str]:
        try:
            list_ = ast.literal_eval(output)
        except Exception as e:
            pass
        else:
            return list_

        output = output.replace("Output:", "").strip()
        output = output.replace("```JSON", "").strip()
        try:
            end_point = output.index("```")
        except ValueError as e:
            raise TokenLimitError(e)
        else:
            output = output.replace("```", "").strip()

        try:
            list_ = ast.literal_eval(output)
        except Exception as e:
            raise StructuredFormatError(e)
        else:
            return list_

    def _make_format(self, props):
        formatter = Formatter
        items = ["meta"]+props
        items = ["_".join(item.split(" ")) for item in items]

        formatted_props = ""
        for item in items:
            item = '\n'.join(['    ' + line for line in formatter.structured_data[item].split('\n')])
            formatted_props += "\n"+item

        example = f"""Format: ```JSON
{{{formatted_props}
}}
```"""
        return example

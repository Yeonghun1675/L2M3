import ast
import json
import regex
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.manager import CallbackManagerForChainRun

from llm_miner.synthesis.prompt import PROMPT_TYPE, PROMPT_STRUCT
from llm_miner.reader.parser.base import Paragraph
from llm_miner.error import StructuredFormatError, LangchainError, TokenLimitError
from llm_miner.format import Formatter
from llm_miner.pricing import TokenChecker, update_token_checker


class SynthesisMiningAgent(Chain):
    type_chain: LLMChain
    type_struct: LLMChain
    input_key: str = "element"
    output_key: str = "output"

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]
    
    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]
    
    def _write_log(self, text: str, run_manager):
        run_manager.on_text(f"\n[Synthesis Mining] ", verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color="yellow")

    def _parse_output(self, output: str) -> Dict[str, str]:
        output = output.replace("```JSON", "")
        output = output.replace("```", "")
        output = output.strip()

        if regex.search(r"[Ii] do not know", output):
            return [output]
        try:
            data = ast.literal_eval(output)
            if isinstance(data, list):
                return data
            else:
                return [data]
        except Exception as e:
            raise StructuredFormatError(e, output)
    
    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()
        
        element: Paragraph = inputs[self.input_key]
        token_checker: TokenChecker = inputs.get('token_checker')
        paragraph: str = element.content

        llm_kwargs={
            'paragraph': paragraph,
        }
        try:
            llm_output = self.type_chain.run(
                **llm_kwargs,
                callbacks=callbacks,
                stop=["Paragraph:"]
            )
        except Exception as e:
            raise LangchainError(e)

        if token_checker:
            update_token_checker(
                name_step='text-synthesis-type',
                chain=self.type_chain,
                token_checker=token_checker,
                llm_kwargs=llm_kwargs,
                llm_output=llm_output
            )

        synthesis_type = self._parse_output(llm_output)
        self._write_log(str(synthesis_type), _run_manager)
        element.set_include_properties(synthesis_type)

        prop_string = ""
        for prop in synthesis_type:
            try:
                structure = Formatter.operation[prop]
            except KeyError:
                self._write_log(f"There are no operation information for {prop}", _run_manager)
                continue
            prop_string += f"- {structure}\n"

        llm_kwargs={
            'paragraph': paragraph,
            'synthesis_type': synthesis_type,
            'format': prop_string,
        }

        try:
            llm_output = self.type_struct.run(
                **llm_kwargs,
                callbacks=callbacks,
                stop=["Paragraph:"]
            )
        except Exception as e:
            raise LangchainError(e)

        if token_checker:
            update_token_checker(
                name_step='text-synthesis-struct',
                chain=self.type_struct,
                token_checker=token_checker,
                llm_kwargs=llm_kwargs,
                llm_output=llm_output
            )

        output = self._parse_output(llm_output)
        self._write_log(json.dumps(output), _run_manager)
        element.set_data(output)

        return {"output": output}

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        prompt_type: str = PROMPT_TYPE,
        prompt_struct: str = PROMPT_STRUCT,
        **kwargs,
    ) -> Chain:
        template_type = PromptTemplate(
            template=prompt_type,
            input_variables=["paragraph"],
            partial_variables={"list_operation": str(Formatter.operation.list_keys())},
        )
        template_struct = PromptTemplate(
            template=prompt_struct,
            input_variables=["synthesis_type", "paragraph", "format"],
        )

        type_chain = LLMChain(llm=llm, prompt=template_type)
        type_struct = LLMChain(llm=llm, prompt=template_struct)

        return cls(
            type_chain=type_chain,
            type_struct=type_struct,
            **kwargs
        )
    
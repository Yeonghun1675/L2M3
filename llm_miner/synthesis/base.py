import json
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.manager import CallbackManagerForChainRun

from llm_miner.synthesis.prompt import PROMPT_TYPE, PROMPT_STRUCT, EXAMPLE_STRUCT
from llm_miner.error import StructuredFormatError


class SynthesisMiningAgent(Chain):
    type_chain: LLMChain
    type_struct: LLMChain
    input_key: str = "paragraph"
    output_key: str = "output"

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]
    
    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]
    
    def _write_log(self, text: str, run_manager):
        run_manager.on_text(f'\n[Synthesis Mining] ', verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color='yellow')

    def _parse_output(self, output: str) -> Dict[str, str]:
        output = output.replace("List:", "").strip()  # remove `List`
        try:
            return json.loads(output)
        except Exception as e:
            raise StructuredFormatError(e)
    
    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()
        
        paragraph = inputs[self.input_key]
        llm_output = self.type_chain.run(
            paragraph = paragraph,
            callbacks=callbacks,
            stop=["Paragraph:"]
        )
        synthesis_type = self._parse_output(llm_output)
        self._write_log(str(synthesis_type), _run_manager)

        llm_output = self.type_struct.run(
            paragraph=paragraph,
            prop=None,
            synthesis_type=synthesis_type,
            callbacks=callbacks,
            stop=['Paragraph:']
        )
        output = self._parse_output(llm_output)
        self._write_log(json.dumps(output), _run_manager)

        return {"output": output}

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        prompt_type: str = PROMPT_TYPE,
        prompt_struct: str = PROMPT_STRUCT,
        example_struct: str = EXAMPLE_STRUCT,
        **kwargs,
    ) -> Chain:
        
        template_type = PromptTemplate(
            template=prompt_type,
            input_variables=['paragraph'],
        )
        template_struct = PromptTemplate(
            template=prompt_struct,
            input_variables=['prop', 'synthesis_type', 'paragraph'],
            partial_variables={'example': example_struct},
        )

        type_chain = LLMChain(llm=llm, prompt=template_type)
        type_struct = LLMChain(llm=llm, prompt=template_struct)

        return cls(
            type_chain=type_chain,
            type_struct=type_struct,
            **kwargs
        )
    
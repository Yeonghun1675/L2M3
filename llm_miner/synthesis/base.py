from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.manager import CallbackManagerForChainRun

from llm_miner.synthesis.prompt import PROMPT


class SynthesisMiningAgent(Chain):
    llm_chain: LLMChain
    input_key: str = "paragraph"
    output_key: str = "output"

    @property
    def input_key(self) -> List[str]:
        return [self.input_key]
    
    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]
    
    def _write_log(self, action: str, text: str, run_manager):
        run_manager.on_text(f'\n[Synthesis Mining] {action}: ', verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color='yellow')

    def _parse_output(self, output: str) -> Dict[str, str]:
        pass
    
    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()
        
        query = inputs[self.input_key]
        self.llm_chain.run(
            paragraph = 'paragraph',
            callbacks=callbacks,
        )

        raise NotImplementedError()
    
    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        prompt: str = PROMPT,
        **kwargs,
    ) -> Chain:
        
        template = PromptTemplate(
            tempate=prompt,
            input_variables=['paragraph'],
        )
        llm_chain = LLMChain(llm, prompt=template)
        return cls(llm_chain=llm_chain, **kwargs)
from typing import Any, Dict, List, Optional
from langchain.chains.base import Chain
from langchain.base_language import BaseLanguageModel
from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks.manager import CallbackManagerForChainRun


class TableMiningAgent(Chain):
    llm: BaseLanguageModel
    input_key: str = "paragraph"
    output_key: str = "output"

    @property
    def input_key(self) -> List[str]:
        return [self.input_key]
    
    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]
    
    def _write_log(self, action, text, run_manager):
        run_manager.on_text(f'\n[Synthesis Mining] {action}: ', verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color='yellow')
    
    def _call(
            self,
            inputs: Dict[str, Any],
    ) -> Dict[str, Any]:
        
        raise NotImplementedError()
    
    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        **kwargs,
    ) -> Chain:
        NotImplementedError()
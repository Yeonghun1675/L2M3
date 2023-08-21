from typing import Any, Dict, List, Optional
from langchain.chains.base import Chain
from langchain.base_language import BaseLanguageModel
from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks.manager import CallbackManagerForChainRun


class LLMMinerAgent(Chain):
    llm: BaseLanguageModel
    input_key: str = "query"
    output_key: str = "output"

    @property
    def input_key(self) -> List[str]:
        return [self.input_key]
    
    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]
    
    def _call(
            self,
            inputs: Dict[str, Any],
    ) -> Dict[str, Any]:
        raise NotImplementedError()
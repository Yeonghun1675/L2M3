from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.callbacks.manager import CallbackManagerForChainRun

from llm_miner.categorize.base import CategorizeAgent
from llm_miner.synthesis.base import SynthesisMiningAgent
from llm_miner.text.base import TextMiningAgent


class LLMMiner(Chain):
    categorize_agent: Chain
    synthesis_agent: Chain
    property_agent: Chain
    input_key: str = "paragraph"
    output_key: str = "output"

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]
    
    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]
    
    def _write_log(self, action: str, text: str, run_manager):
        run_manager.on_text(f'\n[LLMMiner] {action}: ', verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color='yellow')

    def _parse_output(self, output: str) -> Dict[str, str]:
        raise NotImplementedError()
    
    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()
        
        paragraph = inputs[self.input_key]
        categories = self.categorize_agent.run(
            paragraph=paragraph,
            callbacks=callbacks,
        )

        if 'synthesis condition' in categories:
            output = self.synthesis_agent.run(
                paragraph=paragraph,
                callbacks=callbacks,
            )
        elif 'table' in categories:
            pass
        
        elif 'property' in categories:
            output = self.property_agent.run(
                paragraph=paragraph,
                callbacks=callbacks,
            )

        return {self.output_key: output}
    
    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        simple_llm: BaseLanguageModel,
        **kwargs,
    ) -> Chain:
        categorize_agent = CategorizeAgent.from_llm(simple_llm, **kwargs)
        synthesis_agent = SynthesisMiningAgent.from_llm(llm, **kwargs)
        property_agent = TextMiningAgent.from_llm(llm, **kwargs)

        return cls(
            categorize_agent=categorize_agent,
            synthesis_agent=synthesis_agent,
            property_agent=property_agent,
            **kwargs
        )
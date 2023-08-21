import json
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.callbacks.manager import CallbackManagerForChainRun

from llm_miner.categorize.base import CategorizeAgent


class LLMMiner(Chain):
    categorize_agent: Chain
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
        output = output.replace("List:", "").strip()  # remove `List`
        return json.loads(output)
    
    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        #_run_manager = CallbackManagerForChainRun.get_noop_manager()
        
        paragraph = inputs[self.input_key]
        categories = self.categorize_agent.run(paragraph, run_manager=_run_manager)

        if 'synthesis condition' in categories:
            # sysntehsis_agent.run()
            pass
        elif 'table' in categories:
            pass
            # table_agent.run()
        else:

            pass

        output = categories
        return {self.output_key: output}
    
    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        **kwargs,
    ) -> Chain:

        categorize_agent = CategorizeAgent.from_llm(llm, **kwargs)
        return cls(categorize_agent=categorize_agent, **kwargs)
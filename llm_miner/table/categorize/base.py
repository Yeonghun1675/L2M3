from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.manager import CallbackManagerForChainRun

from llm_miner.table.categorize.prompt import PROMPT_CATEGORIZE
from llm_miner.error import ContextError
from llm_miner.pricing import TokenChecker, update_token_checker


class CategorizeAgent(Chain):
    categorize_chain: LLMChain
    labels: List[str] = ["Crystal", "Bond & Angle", "Coordinate", "Property"]
    input_key: str = "paragraph"
    output_key: str = "output"

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]
    
    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]
    
    def _write_log(self, text: str, run_manager):
        run_manager.on_text(f'\n[Categorize] ', verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color='yellow')

    def _parse_output(self, output: str) -> Dict[str, str]:
        output = output.replace("Output:", "").strip()  # remove `List`
        if output.startswith('\''):
            output = output[1:-1]
        if output.startswith("\""):
            output = output[1:-1]
        return output
    
    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None,
            token_checker: Optional[TokenChecker] = None
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()

        para = inputs[self.input_key]
        token_checker: TokenChecker = inputs['token_checker']

        llm_kwargs={
            'paragraph': para,
        }

        llm_output = self.categorize_chain.run(
            **llm_kwargs,
            callbacks = callbacks,
            stop = ['Input:'],
        )

        if token_checker:
            update_token_checker(
                name_step='table-categorize',
                chain=self.categorize_chain,
                token_checker=token_checker,
                llm_kwargs=llm_kwargs,
                llm_output=llm_output,
            )
            
        output = self._parse_output(llm_output)

        if not output:
            raise ContextError(f'There are no categories in table')
        if output not in self.labels:
            raise ContextError(f'Class of table must be one of {self.labels}, not {output}')

        self._write_log(str(output), _run_manager)

        return {self.output_key: output}
    
    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        prompt: str = PROMPT_CATEGORIZE,
        **kwargs,
    ) -> Chain:
        template = PromptTemplate(
            template=prompt,
            template_format="jinja2",
            input_variables=['paragraph'],
        )
        categorize_chain = LLMChain(llm=llm, prompt=template)
        return cls(categorize_chain=categorize_chain, **kwargs)

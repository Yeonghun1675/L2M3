import ast
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.prompts import PromptTemplate
from langchain.callbacks.manager import CallbackManagerForChainRun

from llm_miner.categorize.prompt import PROMPT_CATEGORIZE, FT_CATEGORIZE, FT_HUMAN
from llm_miner.error import StructuredFormatError, ContextError, LangchainError
from llm_miner.schema import Paragraph
from llm_miner.pricing import TokenChecker, update_token_checker


class CategorizeAgent(Chain):
    categorize_chain: LLMChain
    labels: List[str] = ["table", "figure", "property", "synthesis condition", "else"]
    input_key: str = "paragraph"
    output_key: str = "output"

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]
    
    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]
    
    def _write_log(self, text: str, run_manager):
        run_manager.on_text(f"\n[Categorize] ", verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color="yellow")

    def _parse_output(self, output: str) -> Dict[str, str]:
        output = output.replace("List:", "").strip()  # remove `List`
        try:
            return ast.literal_eval(output)
        except Exception as e:
            raise StructuredFormatError(e)
    
    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()
        
        para: Paragraph = inputs[self.input_key]
        token_checker: TokenChecker = inputs.get('token_checker')

        if para.type in self.labels:
            self._write_log([para.type], _run_manager)
            return {self.output_key: [para.type]}
        
        llm_kwargs={
            'paragraph': str(para.content),
        }
        try:
            llm_output = self.categorize_chain.run(
                **llm_kwargs,
                callbacks = callbacks,
                stop = ["List:"],
            )
        except Exception as e:
            para.add_intermediate_step('categorize', str(e))
            raise LangchainError(e)
        else:
            para.add_intermediate_step('categorize', llm_output)

        if token_checker:
            update_token_checker(
                name_step='categorize',
                chain=self.categorize_chain,
                token_checker=token_checker,
                llm_kwargs=llm_kwargs,
                llm_output=llm_output
            )
        output = self._parse_output(llm_output)
        para.set_classification(output)

        if not output:
            para.add_intermediate_step('categorize-parsing', 'no categories error')
            raise ContextError(f"There are no categories in paragraph")
        if any([v not in self.labels for v in output]):
            para.add_intermediate_step('categorize-parsing', 'not included error')
            raise ContextError(f"Class of paragraph must be one of {self.labels}, not {output}")

        self._write_log(str(output), _run_manager)

        return {self.output_key: output}
    
    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        prompt: str = PROMPT_CATEGORIZE,
        ft_prompt: str = FT_CATEGORIZE,
        ft_human: str = FT_HUMAN,
        **kwargs,
    ) -> Chain:
        
        if llm.model_name.startswith('ft:'): # fine-tuned model
            system_prompt = SystemMessagePromptTemplate.from_template(ft_prompt)
            human_prompt = HumanMessagePromptTemplate.from_template(ft_human)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_prompt, human_prompt]
            )
            categorize_chain = LLMChain(
                llm=llm,
                prompt=chat_prompt,
            )
        else:  # gpt base model
            template = PromptTemplate(
                template=prompt,
                input_variables=["paragraph"],
            )
            categorize_chain = LLMChain(llm=llm, prompt=template)

        return cls(categorize_chain=categorize_chain, **kwargs)

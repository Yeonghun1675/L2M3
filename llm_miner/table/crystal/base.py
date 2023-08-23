import ast
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

from llm_miner.error import StructuredFormatError, TokenLimitError
from llm_miner.format import Formatter
from llm_miner.table.crystal.prompt import CRYSTAL_CATEGORIZE, CRYSTAL_EXTRACT


class CrystalTableAgent(Chain):
    categorize_chain: LLMChain
    extract_chain: LLMChain
    input_key: str = "paragraph"
    output_key: str = "output"
    included_props: list = []

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        prompt_categorize: str = CRYSTAL_CATEGORIZE,
        prompt_extract: str = CRYSTAL_EXTRACT,
        **kwargs,
    ) -> Chain:

        template_categorize = PromptTemplate(
            template=prompt_categorize,
            template_format="jinja2",
            input_variables=['paragraph'],
        )
        categorize_chain = LLMChain(llm=llm, prompt=template_categorize)

        template_extract = PromptTemplate(
            template=prompt_extract,
            template_format="jinja2",
            input_variables=['prop', 'format', 'paragraph'],
        )
        extract_chain = LLMChain(llm=llm, prompt=template_extract)

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

        paragraph = inputs[self.input_key]
        included_props = self.categorize_chain.run(
            paragraph=paragraph,
            callbacks=callbacks,
            stop=["Input:"]
        )
        self.included_props = self._parse_output_props(included_props)
        self._write_log(str(self.included_props), _run_manager)

        props = self.included_props[:]
        if "chemical formula" in props:
            props.remove("chemical formula")
        format = self._make_format(props)
        output = self.extract_chain.run(
            prop=props,
            format=format,
            paragraph=paragraph,
            callbacks=callbacks,
            stop=["Input:"]
        )

        output = self._parse_output_json(output)
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
        output = output.replace("Output:", "").strip()
        try:
            end_point = output.index("<END>")
        except ValueError as e:
            raise TokenLimitError(e)
        else:
            output = output[:end_point].strip()

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

        example = f"""Example:
```
{{{formatted_props}
}}
```"""
        return example

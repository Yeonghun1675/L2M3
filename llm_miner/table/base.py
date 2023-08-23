import ast
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

from llm_miner.error import ContextError, TokenLimitError
from llm_miner.format import Formatter
from llm_miner.table.categorize.base import CategorizeAgent
from llm_miner.table.crystal.base import CrystalTableAgent
from llm_miner.table.property.base import PropertyTableAgent
from llm_miner.table.prompt import CONVERT2MD


class TableMiningAgent(Chain):
    convert_chain: LLMChain
    categorize_agent: Chain
    crystal_table_agent: Chain
    property_table_agent: Chain
    input_key: str = "paragraph"
    output_key: str = "output"

    md_table: str = ""
    table_type: str = ""
    included_props: list = []

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        complex_llm: BaseLanguageModel,
        prompt_convert: str = CONVERT2MD,
        **kwargs,
    ) -> Chain:

        template_convert = PromptTemplate(
            template=prompt_convert,
            input_variables=['paragraph'],
        )
        convert_chain = LLMChain(llm=llm, prompt=template_convert)
        categorize_agent = CategorizeAgent.from_llm(complex_llm, **kwargs)
        crystal_table_agent = CrystalTableAgent.from_llm(complex_llm, **kwargs)
        property_table_agent = PropertyTableAgent.from_llm(complex_llm, **kwargs)

        return cls(
            convert_chain=convert_chain,
            categorize_agent=categorize_agent,
            crystal_table_agent=crystal_table_agent,
            property_table_agent=property_table_agent,
            **kwargs
        )

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]

    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]

    def _write_log(self, action, text, run_manager):
        run_manager.on_text(f'\n[Table Mining] {action}: ', verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color='yellow')

    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()

        paragraph = inputs[self.input_key]
        md_output = self.convert_chain.run(
            paragraph=paragraph,
            callbacks=callbacks,
            stop=["Input:"]
        )
        self.md_table = self._parse_convert_output(md_output)

        self.table_type = self.categorize_agent.run(self.md_table)

        if self.table_type == "Crystal":
            output = self.crystal_table_agent.run(
                paragraph=self.md_table,
                callbacks=callbacks,
            )
            self.included_props = self.crystal_table_agent.included_props
        elif self.table_type in ["Bond & Angle", "Coordinate"]:
            output = f"{self.table_type} type of table is not target"
        elif self.table_type == "Property":
            output = self.property_table_agent.run(
                paragraph=self.md_table,
                callbacks=callbacks,
            )
            self.included_props = self.property_table_agent.included_props
        else:
            raise ContextError("Must be one of [Crytstal, Bond & Angle, Coordinate, Property]")

        return {"output": output}

    def _parse_convert_output(self, output: str):
        output = output.replace("MD table:", "").strip()
        try:
            end_point = output.index("<END>")
        except ValueError as e:
            raise TokenLimitError(e)
        else:
            output = output[:end_point].strip()
            return output

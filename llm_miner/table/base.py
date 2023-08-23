import ast
import json
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
# from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks.manager import CallbackManagerForChainRun
import regex

from llm_miner.table.prompt import CONVERT2MD, CRYSTAL_CATEGORIZE, CRYSTAL_EXTRACT
from llm_miner.error import StructuredFormatError, TokenLimitError


class TableMiningAgent(Chain):
    convert_chain: LLMChain
    crystal_table_agent: Chain
    # property_table_agent: Chain
    input_key: str = "paragraph"
    output_key: str = "output"

    md_table: str = ""
    included_props: list = []
    crystal_pattern = regex.compile(r'\b(Crystallographic|Crystal dat(a|e)|Structure refinement|Structural Refinement|Diffraction experiments)\b', regex.IGNORECASE)
    bond_pattern = regex.compile(r'(Selected\s+)?(Bond\s+)?(lengths|distances|interatomic distances)(\s+\(Å\))?(\s+and\s+bond?\s+angles(\s+\(°|deg\.?\))?(\s+for)?)?|Selected\s+geometric\s+parameters\s+for', regex.IGNORECASE)
    bond_pattern2 = regex.compile(r'\b(Selected geometric parameters|Structural parameters|Crystal and structure refine data|Selected bond angles for)\b', regex.IGNORECASE)
    coordinate_pattern = regex.compile(r'\b(atomic coordinate(s)?|equivalent isotropic atomic displacement)\b', regex.IGNORECASE)

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
        crystal_table_agent = CrystalTableAgent.from_llm(complex_llm, **kwargs)
        # property_table_agent = PropertyTableAgent.from_llm(complex_llm, **kwargs)

        return cls(
            convert_chain=convert_chain,
            crystal_table_agent=crystal_table_agent,
            # property_table_agent=property_table_agent,
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

        table_type = self._classify_md_table()
        if table_type == "Crystal":
            output = self.crystal_table_agent.run(
                paragraph=self.md_table,
                callbacks=callbacks,
            )
            self.included_props = self.crystal_table_agent.included_props
        elif table_type in ["Bond & Angle", "Coordinate"]:
            output = f"{table_type} type of table is not target"
        else:
            output = "property table not defined yet"
            # output = self.property_table_agent.run(
            #     paragraph=self.md_table,
            #     callbacks=callbacks,
            # )

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

    def _classify_md_table(self):
        tmp_table = "\n".join(self.md_table.split("\n")[:4]+self.md_table.split("\n")[-4:])
        if bool(self.crystal_pattern.search(tmp_table)):
            return "Crystal"
        elif (bool(self.bond_pattern.search(tmp_table)) or bool(self.bond_pattern2.search(tmp_table))):
            return "Bond & Angle"
        elif bool(self.coordinate_pattern.search(tmp_table)):
            return "Coordinate"
        else:
            return "Property"


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
        included_props = self.categorize_chain.run(
            paragraph=paragraph,
            callbacks=callbacks,
            stop=["Input:"]
        )
        self.included_props = self._parse_output_props(included_props)

        props = self.included_props[:]
        if "chemical formula" in props:
            props.remove("chemical formula")
        format = self._make_format(props)
        print(format)
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
        prop2struct = {
            "chemical formula weight": """"chemical formula weight": {  # sum of the atomic weights of the elements present in its chemical formula.
        "value": "",
    }""",

            "space group": """"space group": {  # a mathematical description of the symmetries inherent in a periodic crystal lattice.
        "value": "",  # ex) P1
    }""",

            "crystal system": """"crystal system": {  # symmetrical and geometrical arrangements within the crystal lattice of materials.
        "value": "",  # ex) Triclinic
    }""",

            "lattice parameters": """"lattice parameters": {  # cell lengths and angles.
        "value": {
            "a": "",
            "b": "",
            "c": "",
            "alpha": "",
            "beta": "",
            "gamma": "",
        },
    }""",

            "cell volume": """"cell volume": {  # cell volume of materials.
        "value": "",
        "unit": "",  # ex) Å^3
    }""",

            "density": """"density": {  # bulk density of materials.
        "value": "",
        "unit": "",  # ex) g/cm^3
    }""",

            "crystal size": """"crystal size": {  # crystal size of materials.
        "value": "",
        "unit": "",  # ex) mm
    }""",
        }

        formatted_props = ""
        for item in props:
            formatted_props += "\n   " + prop2struct[item]

        example = f"""Example:
```
{{
    "meta": {{
        "name": "",
        "symbol": "",  # ex) 1a
        "chemical formula": "",
    }},{formatted_props}
}}
```"""
        return example

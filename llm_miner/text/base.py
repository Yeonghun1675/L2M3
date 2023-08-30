import ast
import regex
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.callbacks.manager import CallbackManagerForChainRun

from llm_miner.text.prompt import PROMPT_TYPE, PROMPT_EXT
from llm_miner.reader.parser.base import Paragraph
from llm_miner.format import Formatter
from llm_miner.error import StructuredFormatError


class TextMiningAgent(Chain):
    type_chain: LLMChain
    extract_chain: LLMChain
    input_key: str = "element"
    output_key: str = "output"

    @property
    def input_keys(self) -> List[str]:
        return [self.input_key]
    
    @property
    def output_keys(self) -> List[str]:
        return [self.output_key]
    
    def _write_log(self, text: str, run_manager):
        run_manager.on_text(f"\n[Property Mining] ", verbose=self.verbose)
        run_manager.on_text(text, verbose=self.verbose, color="yellow")

    def _parse_output(self, output: str) -> Dict[str, str]:
        output = output.replace("List:", "").strip()  # remove `List`
        if regex.search(r"[Ii] do not know", output):
            return [output]
        try:
            data = ast.literal_eval(output)
            if isinstance(data, list):
                return data
            else:
                return [data]
        except Exception as e:
            raise StructuredFormatError(e, output)
    
    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()

        explanation = self._add_explanation()
        element: Paragraph = inputs[self.input_key]
        paragraph: str = element.content

        llm_output = self.type_chain.run(
            explanation = explanation,
            paragraph = paragraph,
            callbacks=callbacks,
            stop=["Paragraph:"]
        )

        property_type = self._parse_output(llm_output)
        self._write_log(str(property_type), _run_manager)
        element.set_include_properties(property_type)

        output = {}
        for prop in property_type:
            try:
                st_data = Formatter.structured_data[prop]
                info = Formatter.information[prop]
                example = Formatter.example_text[prop]
            except KeyError:
                self._write_log(f"There are no format for {prop}", _run_manager)
                continue

            llm_output = self.extract_chain.run(
                prop=prop,
                structured_data=st_data,
                information=info,
                example=example,
                paragraph=paragraph,
                callbacks=callbacks,
            )

            st_output = self._parse_output(llm_output)
            self._write_log(f"{prop} : {st_output}", _run_manager)
            output[prop] = st_output

        element.set_data(output)
        return {"output": output}
    
    def _add_explanation(self):
        erase_list = [
            "cell_volume",
            "lattice_parameters",
            "conversion",
            "reaction_yield",
            "chemical_formula",
        ]
        formatter = Formatter
        target_items = list(formatter.explanation.keys())
        target_items = [item for item in target_items if item not in erase_list]
        explained_props = ""
        for item in target_items:
            explained_props += "\n" + f"- {item}: " + formatter.explanation[item].strip()
        return explained_props.strip()

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        prompt_type: str = PROMPT_TYPE,
        prompt_extract: str = PROMPT_EXT,
        **kwargs,
    ) -> Chain:
        
        template_type = PromptTemplate(
            template=prompt_type,
            input_variables=["explanation", "paragraph"],
        )
        template_extract = PromptTemplate(
            template=prompt_extract,
            input_variables=["prop", "structured_data", "information", "example", "paragraph"],
        )

        type_chain = LLMChain(llm=llm, prompt=template_type)
        extract_chain = LLMChain(llm=llm, prompt=template_extract)

        return cls(
            type_chain=type_chain,
            extract_chain=extract_chain,
            **kwargs
        )
    
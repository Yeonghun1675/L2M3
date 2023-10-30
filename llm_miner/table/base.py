import regex
from typing import Any, Dict, List, Optional

from langchain.base_language import BaseLanguageModel
from langchain.callbacks.manager import CallbackManagerForChainRun
from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from llm_miner.error import ContextError, TokenLimitError, LangchainError
from llm_miner.schema import Paragraph
from llm_miner.table.categorize.base import CategorizeAgent
from llm_miner.table.crystal.base import CrystalTableAgent
from llm_miner.table.property.base import PropertyTableAgent
from llm_miner.table.prompt import CONVERT2MD, FT_CONVERT, FT_HUMAN
from llm_miner.pricing import TokenChecker, update_token_checker


class TableMiningAgent(Chain):
    convert_chain: LLMChain
    emergency_chain: LLMChain

    categorize_agent: Chain
    crystal_table_agent: Chain
    property_table_agent: Chain
    input_key: str = "element"
    output_key: str = "output"

    md_table: str = ""
    table_type: str = ""
    included_props: list = []

    @classmethod
    def from_llm(
        cls,
        convert_llm: BaseLanguageModel,
        emergency_llm: BaseLanguageModel,
        categorize_llm: BaseLanguageModel,
        crystal_table_type_llm: BaseLanguageModel,
        crystal_table_extract_llm: BaseLanguageModel,
        property_table_type_llm: BaseLanguageModel,
        property_table_extract_llm: BaseLanguageModel,
        *,
        prompt_convert: str = CONVERT2MD,
        ft_convert: str = FT_CONVERT,
        ft_human: str = FT_HUMAN,
        **kwargs,
    ) -> Chain:
        if convert_llm.model_name.startswith('ft:'): # fine-tuned model
            system_prompt = SystemMessagePromptTemplate.from_template(ft_convert)
            human_prompt = HumanMessagePromptTemplate.from_template(ft_human)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_prompt, human_prompt]
            )
            convert_chain = LLMChain(
                llm=convert_llm,
                prompt=chat_prompt,
            )
        else:
            template_convert = PromptTemplate(
                template=prompt_convert,
                input_variables=['paragraph'],
            )
            convert_chain = LLMChain(llm=convert_llm, prompt=template_convert)

        emergency_convert = PromptTemplate(template=prompt_convert, input_variables=['paragraph'])
        emergency_chain = LLMChain(llm=emergency_llm, prompt=emergency_convert)

        categorize_agent = CategorizeAgent.from_llm(categorize_llm, **kwargs)
        crystal_table_agent = CrystalTableAgent.from_llm(crystal_table_type_llm, crystal_table_extract_llm, **kwargs)
        property_table_agent = PropertyTableAgent.from_llm(property_table_type_llm, property_table_extract_llm, **kwargs)

        return cls(
            convert_chain=convert_chain,
            emergency_chain=emergency_chain,
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

    @staticmethod
    def remove_attributes(xml_str):
        # Remove xmlns, id, view, nameend, namest, and valign attributes
        cleaned_xml = regex.sub(r' (xmlns|id|view|nameend|namest|valign)="[^"]+"', '', xml_str)

        # Remove hsp, vsp, and colspec elements
        cleaned_xml = regex.sub(r'<(ce:)?hsp[^>]*>.*?</(ce:)?hsp>', '', cleaned_xml)
        cleaned_xml = regex.sub(r'<vsp[^>]*>.*?</vsp>', '', cleaned_xml)
        cleaned_xml = regex.sub(r'<colspec[^>]*>.*?</colspec>', '', cleaned_xml)

        # Remove ce:italic, ce:bold, italic, and bold tags but keep their content
        cleaned_xml = regex.sub(r'<(ce:)?italic>(.*?)</(ce:)?italic>', r'\2', cleaned_xml)
        cleaned_xml = regex.sub(r'<(ce:)?bold>(.*?)</(ce:)?bold>', r'\2', cleaned_xml)

        # Remove MathML elements
        # cleaned_xml = regex.sub(r'<mml:math.*?>.*?</mml:math>', '', cleaned_xml, flags=regex.DOTALL)

        # Remove <inf loc="post"> tags and their content
        cleaned_xml = regex.sub(r'<(ce:)?inf loc="post">(.*?)</(ce:)?inf>', r'\2', cleaned_xml)
        cleaned_xml = regex.sub(r' (frame|loc)="[^"]+"', '', cleaned_xml)

        # Remove multiple enters
        cleaned_xml = regex.sub(r'\n+', '\n', cleaned_xml)
        return cleaned_xml

    def _call(
            self,
            inputs: Dict[str, Any],
            run_manager: Optional[CallbackManagerForChainRun] = None
    ) -> Dict[str, Any]:
        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        callbacks = _run_manager.get_child()

        element: Paragraph = inputs[self.input_key]
        token_checker: TokenChecker = inputs['token_checker']
        paragraph: str = TableMiningAgent.remove_attributes(element.content)

        llm_kwargs = {
            'paragraph': paragraph
        }
        try:
            md_output = self.convert_chain.run(
                **llm_kwargs,
                callbacks=callbacks,
                stop=["Input:"]
            )
        except Exception as e:
            element.add_intermediate_step('table-convert2MD', str(e))
        else:
            element.add_intermediate_step('table-convert2MD', "[gpt.ft]"+md_output)

        try:
            md_table = self._parse_convert_output(md_output)
            element.set_clean_text(md_table)
            if token_checker:
                update_token_checker(
                    name_step='table-conver2MD',
                    chain=self.convert_chain,
                    token_checker=token_checker,
                    llm_kwargs=llm_kwargs,
                    llm_output=md_output,
                )
        except (TokenLimitError, UnboundLocalError):
            try:
                print("non-ft model try: due to token limit")
                md_output = self.emergency_chain.run(
                    **llm_kwargs,
                    callbacks=callbacks,
                    stop=["Input:"]
                )
            except Exception as e:
                element.add_intermediate_step('table-convert2MD', str(e))
                raise LangchainError(e)
            else:
                element.add_intermediate_step('table-convert2MD', "[gpt3.5]"+md_output)

            try:
                md_table = self._parse_convert_output(md_output)
                element.set_clean_text(md_table)
            except Exception as e:
                element.add_intermediate_step('table-convert2MD', str(e))
                raise TokenLimitError
            else:
                if token_checker:
                    update_token_checker(
                        name_step='table-conver2MD',
                        chain=self.emergency_chain,
                        token_checker=token_checker,
                        llm_kwargs=llm_kwargs,
                        llm_output=md_output,
                    )

        if md_table == "Empty content":
            table_type = "None"

        else:
            table_type = self.categorize_agent.run(
                #paragraph=md_table,
                element=element,
                callbacks=callbacks,
                token_checker=token_checker
            )
            table_type = str(table_type)
        element.set_classification(table_type)

        if table_type == "Crystal":
            output = self.crystal_table_agent.run(
                #paragraph=md_table,
                element=element,
                callbacks=callbacks,
                token_checker=token_checker
            )
            props = self.crystal_table_agent.included_props
            element.set_include_properties(props)
        elif table_type in ["Bond & Angle", "Coordinate", "Elemental Composition"]:
            output = [f"{table_type} type of table is not target"]
        elif table_type == "Property":
            output = self.property_table_agent.run(
                #paragraph=md_table,
                element=element,
                callbacks=callbacks,
                token_checker=token_checker
            )
            props = self.property_table_agent.included_props
            element.set_include_properties(props)
        elif table_type == "None":
            output = ["Table seems to be empty"]
        else:
            raise ContextError("Must be one of [Crytstal, Bond & Angle, Coordinate, Property, Elemental Composition]")

        element.set_data(output)
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

from typing import Any, Dict, List, Optional

from langchain.chat_models import ChatOpenAI       
from langchain.base_language import BaseLanguageModel
from langchain.chains.base import Chain
from langchain.callbacks.manager import CallbackManagerForChainRun

from llm_miner.config import config
from llm_miner.reader import JournalReader
from llm_miner.categorize.base import CategorizeAgent
from llm_miner.synthesis.base import SynthesisMiningAgent
from llm_miner.text.base import TextMiningAgent
from llm_miner.table.base import TableMiningAgent
from llm_miner.error import BaseMiningError

from llm_miner.pricing import TokenChecker


class LLMMiner(Chain):
    categorize_agent: Chain
    synthesis_agent: Chain
    table_agent: Chain
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

        jr: JournalReader = inputs[self.input_key]
        token_checker: TokenChecker = inputs.get('token_checker')

        for element in jr.elements:
            try:
                categories = self.categorize_agent.run(
                    paragraph=element,
                    callbacks=callbacks,
                    token_checker=token_checker,
                )
            except BaseMiningError:
                element.classification = 'error'

            # print (categories)
        
        # reconstruct elements -> merge paragraph for reducing tokens
        if config.get('reconstruct'):
            jr.reconstruct()

        for element in jr.get_synthesis_conditions():
            try:
                output = self.synthesis_agent.run(
                    element=element,
                    callbacks=callbacks,
                    token_checker=token_checker
                )
            except BaseMiningError as e:
                element.set_data([str(e)])
            else:
                pass
                # print (output)

        for element in jr.get_properties():
            try:
                output = self.property_agent.run(
                    element=element,
                    callbakcs=callbacks,
                    token_checker = token_checker
                )
            except BaseMiningError as e:
                element.set_data([str(e)])
            else:
                pass
                # print (output)


        for element in jr.get_tables():
            try:
                output = self.table_agent.run(
                    element=element,
                    callbakcs=callbacks,
                    token_checker = token_checker
                )
            except BaseMiningError as e:
                element.set_data([str(e)])
            # print (output)


        if config['reconstruct']:
            return {self.output_key: jr.cln_elements}
        else:
            return {self.output_key: jr.elements}

    @classmethod
    def from_llm(
        cls,
        llm: BaseLanguageModel,
        simple_llm: BaseLanguageModel,
        *,
        ft_model_dict: Optional[Dict[str, BaseLanguageModel]] = None,
        **kwargs,
    ) -> Chain:
        if ft_model_dict is None:
            ft_model_dict = dict()

        categorize_agent = CategorizeAgent.from_llm(
            llm = ft_model_dict.get('ft_text_categorize', simple_llm), 
            **kwargs
        )

        synthesis_agent = SynthesisMiningAgent.from_llm(
            type_llm = ft_model_dict.get('ft_text_synthesis_type', llm), 
            extract_llm = ft_model_dict.get('ft_text_synthesis_extract', llm),
            **kwargs
        )

        property_agent = TextMiningAgent.from_llm(
            type_llm = ft_model_dict.get('ft_text_property_type', llm), 
            extract_llm = ft_model_dict.get('ft_text_property_extract', llm),
            **kwargs
        )

        table_agent = TableMiningAgent.from_llm(
            convert_llm = ft_model_dict.get('ft_table_convert', llm),
            categorize_llm = ft_model_dict.get('ft_table_categorize', llm),
            crystal_table_type_llm = ft_model_dict.get('ft_table_crystal_type', llm),
            crystal_table_extract_llm=llm,
            property_table_type_llm= ft_model_dict.get('ft_table_property_type', llm),
            property_table_extract_llm=llm,
            **kwargs
        )
        
        return cls(
            categorize_agent=categorize_agent,
            table_agent=table_agent,
            synthesis_agent=synthesis_agent,
            property_agent=property_agent,
            **kwargs
        )
    
    @classmethod
    def from_config(
        cls,
        config: Dict[str, Any],
    ) -> Chain:
        model_name = config['model_name']
        simple_model_name = config['simple_model_name']
        temperature = config['temperature']

        llm = ChatOpenAI(
            model_name = model_name,
            temperature = temperature
        )
        simple_llm = ChatOpenAI(
            model_name = simple_model_name,
            temperature = temperature
        )

        # fine-tuned model
        ft_model_dict = {
            ft_name: ChatOpenAI(model_name=ft_model, temperature=temperature)
            for ft_name, ft_model in config['fine_tuning_models'].items() if ft_model
        }

        return cls.from_llm(
            llm=llm,
            simple_llm=simple_llm,
            ft_model_dict = ft_model_dict,
            verbose=config['verbose']
        )
    
    @classmethod
    def create(cls, ):
        """Auto creation using config (default)"""
        return cls.from_config(config)

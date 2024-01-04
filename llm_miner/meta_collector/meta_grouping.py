from typing import Dict, List, Any, Optional
from pydantic import BaseModel

from llm_miner.schema import Elements

# from llm_miner.reader import JournalReader
from llm_miner.meta_collector.base import MinedData, Results
from llm_miner.meta_collector.utils import flatten_list_of_dicts


class MetaCollector(BaseModel):
    list_data: List[MinedData]
    doi: Optional[str]

    def run(
        self,
    ) -> Results:  # before : categorize_by_equality
        results = Results.empty(doi=self.doi)
        for idx, data in enumerate(self.list_data):
            results.append(data, idx)
        return results

    @classmethod
    def from_elements(cls, elements: Elements, doi: Optional[str] = None):
        list_data = []
        for element in elements:
            if not element.has_data():
                continue
            elif element.type == "text":
                formula_source = element.classification
            else:
                formula_source = element.type

            for data in flatten_list_of_dicts(element.data):
                if isinstance(data, str):
                    continue
                elif "meta" not in data:
                    continue
                mined_data = MinedData.from_data(
                    data,
                    formula_source=formula_source,
                    element_idx=element.idx,
                    doi=doi,
                )
                list_data.append(mined_data)

        return cls(list_data=list_data, doi=doi)

    @classmethod
    def from_journal_reader(cls, jr: object):
        if jr.cln_elements:
            elements = jr.cln_elements
        else:
            elements = jr.elements
        return cls.from_elements(elements=elements, doi=jr.doi)

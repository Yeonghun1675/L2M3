import inspect
from typing import Dict, Iterable
from collections.abc import Mapping
from llm_miner.format import structured_data as st_data
from llm_miner.format import explanation as explain_data
from llm_miner.format import information as info_data
from llm_miner.format import example_table
from llm_miner.format import example_text
from llm_miner.format import operation


class BaseFormatter(Mapping):
    data: Dict[str, str]

    def __getitem__(self, idx: str) -> str:
        return self.data[idx].strip()

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)
    
    def list_keys(self):
        return list(self.data.keys())


class BaseStucturedData(BaseFormatter):
    data: Dict[str, str] = {
        name: obj for name, obj in inspect.getmembers(st_data)
        if isinstance(obj, str) and "__" not in name
    }


class BaseExplanation(BaseFormatter):
    data: Dict[str, str] = {
        name: obj for name, obj in inspect.getmembers(explain_data)
        if isinstance(obj, str) and "__" not in name
    }


class BaseInformation(BaseFormatter):
    data: Dict[str, str] = {
        name: obj for name, obj in inspect.getmembers(info_data)
        if isinstance(obj, str) and "__" not in name
    }


class BaseExampleTable(BaseFormatter):
    data: Dict[str, str] = {
        name: obj for name, obj in inspect.getmembers(example_table)
        if isinstance(obj, dict) and "__" not in name
    }

    def __getitem__(self, idx: str) -> dict:
        return self.data[idx]


class BaseExampleText(BaseFormatter):
    data: Dict[str, str] = {
        name: obj for name, obj in inspect.getmembers(example_text)
        if isinstance(obj, str) and "__" not in name
    }


class BaseOperation(BaseFormatter):
    data: Dict[str, str] = {
        name: obj for name, obj in inspect.getmembers(operation)
        if isinstance(obj, str) and "__" not in name
    }


class Formatter(object):
    structured_data = BaseStucturedData()
    explanation = BaseExplanation()
    information = BaseInformation()
    example_table = BaseExampleTable()
    example_text = BaseExampleText()
    operation = BaseOperation()

    @classmethod
    def keys(cls, ) -> Iterable[str]:
        return [
            'structured_data',
            'explanation',
            'information',
            'example_table',
            'example_text',
            'operation'
        ]

import inspect
from typing import Dict
from collections.abc import Mapping
from llm_miner.format import structured_data as st_data


class BaseFormatter(Mapping):    
    structured_data: Dict[str, str] = {
        name: obj for name, obj in inspect.getmembers(st_data) 
        if isinstance(obj, str) and "__" not in name
    }
    
    def __getitem__(self, idx: str) -> str:
        return self.structured_data[idx].strip()
    
    def __iter__(self):
        return iter(self.structured_data)
    
    def __len__(self):
        return len(self.data)
    

Formatter = BaseFormatter()

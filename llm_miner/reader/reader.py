import warnings
from typing import List, Any
from pydantic import BaseModel
from pathlib import Path

from llm_miner.reader.parser.base import Paragraph, Metadata, BaseParser
from llm_miner.reader.parser.elsevier import ElsevierParser
from llm_miner.reader.parser.acs import ACSParser
from llm_miner.reader.parser.rsc import RSCParser
from llm_miner.reader.parser.springer import SpringerParser
from llm_miner.reader.parser.utils import publisher_finder
from llm_miner.error import ReaderError

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


parser_dict = {
    'elsevier': ElsevierParser,
    'acs': ACSParser,
    'rsc': RSCParser,
    'springer': SpringerParser,
}


class JournalReader(BaseModel):
    filepath: Path
    publisher: str
    elements: List[Paragraph]
    metadata: Metadata

    @property
    def filename(self):
        return self.filepath.name.strip()
    
    @property
    def doi(self):
        return self.metadata.doi.strip()
    
    @property
    def title(self):
        return self.metadata.title.strip()
    
    @property
    def url(self):
        return f'https://doi.org/{self.doi}'
    
    def get_tables(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == 'table'] 
            
    def get_texts(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == 'text'] 
                
    def get_figures(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == 'figure'] 
    
    @classmethod
    def from_file(cls, filepath: str, publisher: str = None):
        if publisher is None:
            publisher = publisher_finder(filepath)

        publisher = publisher.lower()
        if publisher not in parser_dict:
            raise ReaderError(f'publisher must be one of [`acs`, `rsc`, `elsevier`, `springer], not {publisher}')

        parser: BaseParser = parser_dict[publisher]
        file_bs = parser.open_file(filepath)
        
        elements = parser.parsing(file_bs)
        metadata = parser.get_metadata(file_bs)

        return cls(
            filepath=Path(filepath),
            publisher=publisher,
            elements=elements,
            metadata=metadata,
        )


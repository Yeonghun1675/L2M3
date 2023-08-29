import warnings
from typing import List, Any, Dict
from pydantic import BaseModel
from pathlib import Path

from llm_miner.reader.parser.base import Paragraph, Elements, Metadata, BaseParser
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
    elements: Elements
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
        return self.elements.get_tables()
            
    def get_texts(self) -> List[Paragraph]:
        return self.elements.get_texts()
                
    def get_figures(self) -> List[Paragraph]:
        return self.elements.get_figures()
    
    def get_synthesis_conditions(self) -> List[Paragraph]:
        return self.elements.get_synthesis_conditions()
    
    def get_properties(self) -> List[Paragraph]:
        return self.elements.get_properties()
    
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
            elements=Elements(elements=elements),
            metadata=metadata,
        )
    
    def to_json(self,) -> Dict[str, Any]:
        return {
            'filepath': self.filepath,
            'publisher': self.publisher,
            'elements': self.elements.to_json(),
            'metadata': self.metadata.to_json(),
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            filepath=data['filepath'],
            publisher=data['publisher'],
            elements=Elements.from_json(data['elements']),
            metadata=Metadata.from_json(data['metadata'])
        )

import warnings
from typing import List
from pydantic import BaseModel
from pathlib import Path

from llm_miner.reader.parser.base import Paragraph, Metadata, BaseParser
from llm_miner.reader.parser.elsevier import ElsevierParser
from llm_miner.reader.parser.acs import ACSParser
from llm_miner.reader.parser.rsc import RSCParser
from llm_miner.reader.parser.springer import SpringerParser
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
    journal: str
    elements: List[Paragraph]
    metadata: Metadata

    @property
    def filename(self):
        return self.filepath.name
    
    @property
    def doi(self):
        return self.metadata.doi
    
    @property
    def title(self):
        return self.metadata.title
    
    def get_tables(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == 'table'] 
            
    def get_texts(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == 'text'] 
                
    def get_figures(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == 'figure'] 
    
    @classmethod
    def from_file(cls, filepath: str, journal: str):
        journal = journal.lower()
        if journal not in parser_dict:
            raise ReaderError(f'journal must be one of [`acs`, `rsc`, `elsevier`, `springer], not {journal}')

        parser: BaseParser = parser_dict[journal]
        file_bs = parser.open_file(filepath)
        
        elements = parser.parsing(file_bs)
        metadata = parser.get_metadata(file_bs)

        return cls(
            filepath=Path(filepath),
            journal=journal,
            elements=elements,
            metadata=metadata,
        )


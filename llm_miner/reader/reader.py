import warnings
import json
from typing import List, Any, Dict
from pydantic import BaseModel
from pathlib import Path

from llm_miner.reader.parser.base import Paragraph, Elements, Metadata, BaseParser
from llm_miner.reader.parser.elsevier import ElsevierParser
from llm_miner.reader.parser.acs import ACSParser
from llm_miner.reader.parser.rsc import RSCParser
from llm_miner.reader.parser.springer import SpringerParser
from llm_miner.reader.parser.utils import publisher_finder
from llm_miner.utils import num_tokens_from_string, merge_para_by_token
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
    cln_elements: Elements = Elements.empty()
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
<<<<<<< HEAD
        return self.elements.get_tables()

    def get_texts(self) -> List[Paragraph]:
        return self.elements.get_texts()

    def get_figures(self) -> List[Paragraph]:
        return self.elements.get_figures()

    def get_synthesis_conditions(self) -> List[Paragraph]:
        return self.elements.get_synthesis_conditions()

    def get_properties(self) -> List[Paragraph]:
        return self.elements.get_properties()

=======
        if self.cln_elements:
            return self.cln_elements.get_tables()
        else:
            return self.elements.get_tables()
            
    def get_texts(self) -> List[Paragraph]:
        if self.cln_elements:
            return self.cln_elements.get_texts()
        else:
            return self.elements.get_texts()
                
    def get_figures(self) -> List[Paragraph]:
        if self.cln_elements:
            return self.cln_elements.get_figures()
        else:
            return self.elements.get_figures()
    
    def get_synthesis_conditions(self) -> List[Paragraph]:
        if self.cln_elements:
            return self.cln_elements.get_synthesis_conditions()
        else:
            return self.elements.get_synthesis_conditions()
    
    def get_properties(self) -> List[Paragraph]:
        if self.cln_elements:
            return self.cln_elements.get_properties()
        else:
            return self.elements.get_properties()
    
>>>>>>> bd28cb77907c8246f630854b25ad38074d0796cb
    def to_dict(self,) -> Dict[str, Any]:
        return {
            'filepath': str(self.filepath),
            'publisher': self.publisher,
            'elements': self.elements.to_dict(),
            'metadata': self.metadata.to_dict(),
        }
<<<<<<< HEAD

=======
    
>>>>>>> bd28cb77907c8246f630854b25ad38074d0796cb
    def to_json(self, filepath) -> Dict[str, Any]:
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f)

<<<<<<< HEAD
=======
    def reconstruct(
            self, 
            max_tokens: int = 4000, 
            model_name:str = 'gpt-4'
    ) -> None:
        if self.cln_elements:    # clear cln_elements
            self.cln_elements = Elements.empty()

        merge_para_by_token(
            ls_para = self.elements.get_synthesis_conditions(),
            classification = 'synthesis condition',
            max_tokens = max_tokens,
            model_name = model_name,
            elements = self.cln_elements
        )

        merge_para_by_token(
            ls_para = self.elements.get_properties(),
            classification = 'property',
            max_tokens = max_tokens,
            model_name = model_name,
            elements = self.cln_elements
        )

        for table in self.elements.get_tables():
            self.cln_elements.append(table)

        for figure in self.elements.get_figures():
            self.cln_elements.append(figure)

>>>>>>> bd28cb77907c8246f630854b25ad38074d0796cb
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

    @classmethod
    def from_dict(cls, data):
        if 'cln_elements' in data:
            cln_elements = Elements.from_dict(data['cln_elements'])
        else:
            cln_elements = Elements.empty()

        return cls(
            filepath=Path(data['filepath']),
            publisher=data['publisher'],
            elements=Elements.from_dict(data['elements']),
            cln_elements=cln_elements,
            metadata=Metadata.from_dict(data['metadata'])
        )

    @classmethod
    def from_json(cls, filepath):
        with open(filepath) as f:
            data = json.load(f)
        return cls.from_dict(data)


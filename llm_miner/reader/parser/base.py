from pydantic import BaseModel
from typing import List, Any, Dict, Optional
from abc import ABCMeta, abstractclassmethod
from collections.abc import Sequence


class BaseParser(object, metaclass=ABCMeta):
    suffix: str
    parser: str
    para_tags: List[str]
    table_tags: List[str]
    figure_tags: List[str]

    @classmethod
    def all_tags(cls):
        return cls.para_tags + cls.table_tags + cls.figure_tags

    @classmethod
    def check_suffix(cls, suffix):
        return suffix == cls.suffix
    
    @abstractclassmethod
    def open_file(cls, filePath: str):
        raise NotImplementedError()
    
    @abstractclassmethod
    def parsing(cls, file: str):
        raise NotImplementedError()
    
    @abstractclassmethod
    def get_metadata(cls, file: str):
        raise NotImplementedError()


class Paragraph(BaseModel):
    idx: int
    type: str
    content: str
    clean_text: Optional[str] = None
    data: Optional[List[Dict[str, Any]]] = None

    def __getitem__(self, item):
        return getattr(self, item)
    
    def append(self, others):
        self.content += others.content
        self.clean_text += '\n'+others.clean_text

        if isinstance(others.data, list):
            if isinstance(self.data, list):
                self.data += others.data
            else:
                self.data = others.data
    
    def set_data(self, data) -> None:
        self.data = data

    def get_data(self, ) -> List[Dict[str, Any]]:
        return self.data
    
    def to_json(self, ) -> Dict[str, Any]:
        return {
            'idx': self.idx,
            'type': self.type,
            'content': self.content,
            'clean_text': self.clean_text,
            'data': self.data
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            idx=data['idx'],
            type=data['type'],
            content=data['content'],
            clean_text=data['clean_text'],
            data=data['data'],
        )


class Elements(Sequence, BaseModel):
    elements: List[Paragraph]

    def __getitem__(self, idx: int) -> Paragraph:
        return self.elements[idx]
    
    def __len__(self,) -> int:
        return len(self.elements)
    
    def get_tables(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == 'table'] 
    
    def get_texts(self) -> List[Paragraph]:
        text_type = ['text', 'synthesis condition', 'property', 'else']
        return [e for e in self.elements if e.type in text_type] 
    
    def get_figures(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == 'figure'] 
    
    def get_synthesis_conditions(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == 'synthesis condition'] 
    
    def get_properties(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == 'property'] 
    
    def to_json(self, )-> List[Dict[str, Any]]:
        return [
            para.to_json() for para in self.elements
        ]
    
    @classmethod
    def from_json(cls, data: List[Dict[str, Any]]):
        return cls(
            elements=[Paragraph.from_json(d) for d in data]
        )


class Metadata(BaseModel):
    doi: Optional[str] = None
    title: Optional[str] = None
    journal: Optional[str] = None
    date: Optional[str] = None
    author_list: Optional[List[str]] = None

    def __getitem__(self, item):
        return getattr(self, item)
    
    def to_json(self) -> Dict[str, Any]:
        return {
            'doi': self.doi,
            'title': self.title,
            'journal': self.journal,
            'date': self.date,
            'author_list': self.author_list
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            doi=data['doi'],
            type=data['title'],
            journal=data['journal'],
            date=data['date'],
            author_list=data['author_list']
        )
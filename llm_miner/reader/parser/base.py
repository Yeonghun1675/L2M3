from pydantic import BaseModel
from typing import List, Any, Dict
from abc import ABCMeta, abstractclassmethod


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
    clean_text: str
    data: List[Dict[str, Any]] = None

    def __getitem__(self, item):
        return getattr(self, item)
    
    def append(self, others):
        self.content += others.content
        self.clean_text = '\n'+others.clean_text

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


class Metadata(BaseModel):
    doi: str = None
    title: str = None
    journal: str = None
    date: str = None
    author_list: List[str] = None

    def __getitem__(self, item):
        return getattr(self, item)
    
    def to_json(self) -> Dict[str, Any]:
        pass

    @classmethod
    def from_json(cls, data):
        pass
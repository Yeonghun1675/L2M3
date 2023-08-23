from pydantic import BaseModel
from typing import List
from abc import ABCMeta, abstractclassmethod


class BaseParser(BaseModel, metaclass=ABCMeta):
    suffix: str
    parser: str

    @property
    def all_tags(self):
        return self.para_tags, self.table_tags, self.figure_tags

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

    def __getitem__(self, item):
        return getattr(self, item)
    

class Metadata(BaseModel):
    doi: str = None
    title: str = None
    journal: str = None
    date: str = None
    author_list: List[str] = None

    def __getitem__(self, item):
        return getattr(self, item)
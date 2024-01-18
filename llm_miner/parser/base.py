from pydantic import BaseModel
from typing import List, Any, Dict, Optional
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


class Metadata(BaseModel):
    doi: Optional[str] = None
    title: Optional[str] = None
    journal: Optional[str] = None
    date: Optional[str] = None
    author_list: Optional[List[str]] = None

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "doi": self.doi,
            "title": self.title,
            "journal": self.journal,
            "date": self.date,
            "author_list": self.author_list,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            doi=data["doi"],
            title=data["title"],
            journal=data["journal"],
            date=data["date"],
            author_list=data["author_list"],
        )

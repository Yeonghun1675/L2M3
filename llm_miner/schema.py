import pprint
from pydantic import BaseModel
from typing import List, Any, Dict, Optional, Union
from collections.abc import Sequence
import copy
import json


class Paragraph(BaseModel):
    idx: Union[int, str]
    type: str
    classification: Optional[Any] = None
    content: str
    clean_text: Optional[str] = None
    data: Optional[List[Any]] = None
    include_properties: Optional[Any] = None
    intermediate_step: Dict[str, Any] = dict()

    def __getitem__(self, item):
        return getattr(self, item)

    def print(
        self,
    ) -> str:
        string = (
            f"Idx : {self.idx}\n"
            f"Type : {self.type}\n"
            f"Classification: {self.classification}\n"
            f"Content: \n{self.clean_text}\n"
            f"Include Properties : {self.include_properties}\n"
            f"Data :\n{pprint.pformat(self.data, sort_dicts=False)}"
        )
        print(string)

    def merge(self, others, merge_idx=False) -> None:
        if merge_idx:
            self.idx = f"{self.idx}, {others.idx}"
        self.content += others.content
        self.clean_text += "\n\n" + others.clean_text

        if isinstance(others.data, list):
            if isinstance(self.data, list):
                self.data += others.data
            else:
                self.data = others.data

    def has_data(
        self,
    ) -> bool:
        if not self.data:
            return False
        if self.data == "None":
            return False
        else:
            return True

    def add_intermediate_step(self, step: str, output: str) -> None:
        self.intermediate_step[step] = output

    def set_data(self, data) -> None:
        if not isinstance(data, list):  # data must be list, not other types
            data = [data]

        if self.data is None:
            self.data = data
        else:
            self.data += data

    def get_data(
        self,
    ) -> List[Dict[str, Any]]:
        return self.data

    def get_intermediate_step(
        self,
    ) -> Dict[str, Any]:
        return self.intermediate_step

    def set_classification(self, cls) -> None:
        if self.classification is None:
            if isinstance(cls, str):
                self.classification = [cls]
            else:
                self.classification = cls
        else:
            if isinstance(cls, str):
                self.classification += [cls]
            else:
                self.classification += cls

    def set_clean_text(self, text) -> None:
        self.clean_text = text

    def set_include_properties(self, props: List[Any]) -> None:
        if self.include_properties is None:
            self.include_properties = props
        else:
            self.include_properties += props

    def copy(
        self,
    ):
        return copy.deepcopy(self)

    def clear(
        self,
    ) -> None:
        self.data = None
        self.include_properties = None
        self.intermediate_step = dict()

    def to_dict(
        self,
    ) -> Dict[str, Any]:
        return {
            "idx": self.idx,
            "type": self.type,
            "classification": self.classification,
            "content": self.content,
            "clean_text": self.clean_text,
            "data": self.data,
            "include_properties": self.include_properties,
            "intermediate_step": self.intermediate_step,
        }

    def to_json(self, filepath) -> Dict[str, Any]:
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            idx=data["idx"],
            type=data["type"],
            classification=data["classification"],
            content=data["content"],
            clean_text=data["clean_text"],
            data=data["data"],
            include_properties=data["include_properties"],
            intermediate_step=data.get("intermediate_step", dict()),
        )

    @classmethod
    def from_json(cls, filepath):
        with open(filepath) as f:
            data = json.load(f)
        return cls.from_dict(data)


class Elements(Sequence, BaseModel):
    elements: List[Paragraph]

    def __getitem__(self, idx: int) -> Paragraph:
        return self.elements[idx]

    def __len__(
        self,
    ) -> int:
        return len(self.elements)

    def __bool__(self) -> bool:
        return bool(self.elements)

    def get_tables(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == "table"]

    def get_texts(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == "text"]

    def get_figures(self) -> List[Paragraph]:
        return [e for e in self.elements if e.type == "figure"]

    def get_synthesis_conditions(self) -> List[Paragraph]:
        return [
            e
            for e in self.elements
            if e.classification and "synthesis condition" in e.classification
        ]

    def get_properties(self) -> List[Paragraph]:
        return [
            e
            for e in self.elements
            if e.classification and "property" in e.classification
        ]

    def to_dict(
        self,
    ) -> List[Dict[str, Any]]:
        return [para.to_dict() for para in self.elements]

    def to_json(self, filepath) -> Dict[str, Any]:
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f)

    def append(self, para: Paragraph) -> None:
        self.elements.append(para)

    @classmethod
    def empty(
        cls,
    ):
        return cls(elements=list())

    @classmethod
    def from_dict(cls, data: List[Dict[str, Any]]):
        return cls(elements=[Paragraph.from_dict(d) for d in data])

    @classmethod
    def from_json(cls, filepath):
        with open(filepath) as f:
            data = json.load(f)
        return cls.from_dict(data)
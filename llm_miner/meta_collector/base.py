import pprint
from pydantic import BaseModel
from typing import List, Any, Dict, Optional, Union
from collections.abc import Sequence
import json
from llm_miner.schema import Paragraph
from llm_miner.meta_collector.utils import format_chemical_formula, format_chemical_name


class Material(BaseModel):
    name: Optional[str] = None
    symbol: Optional[str] = None
    chemical_formula: Optional[str] = None
    formula_source: Optional[str] = None

    @property
    def clean_chemical_formula(
        self,
    ) -> (str, bool):
        formula, is_general = format_chemical_formula(self.chemical_formula)
        return formula, is_general

    def is_equal(self, other: object) -> bool:
        s_formula, _ = self.clean_chemical_formula
        o_formula, _ = other.clean_chemical_formula

        if self.name:
            if self.name == other.name or self.name == other.symbol:
                if (
                    s_formula != o_formula
                    and self.formula_source == other.formula_source
                ):
                    return False
                return True
        if self.symbol:
            if self.symbol == other.symbol or self.symbol == other.name:
                return True
        else:
            return False

    def concatenate(self, others: object) -> None:  # before: concatenate_data
        # 같은 meta를 가지는 두 물질 정보를 합쳐서 하나의 물질 정보로 만들기 # should be revised
        s_formula, s_general = self.clean_chemical_formula
        o_formula, o_general = others.clean_chemical_formula
        if s_general:
            self.chemical_formula = s_formula

        if self.name == others.symbol:
            if others.name:
                self.name = others.name
            self.symbol = others.symbol

        if others.formula_source != "synthesis condition" and o_general:
            self.chemical_formula = o_formula
            self.formula_source = others.formula_source

        if not self.name:
            self.name = others.name
        if not self.symbol:
            self.symbol = others.symbol
        if not self.chemical_formula:
            self.chemical_formula = o_formula
            self.formula_source = others.formula_source

    @classmethod
    def from_data(cls, data: Dict[str, Any], formula_source: Optional[str] = None):
        """
        근데 이렇게 바로 넣으면 원래가 뭐였는지 확인이 좀 어렵더라.
        """
        if not formula_source:
            formula_source = data.get("formula source")
        chemical_formula = data.get("chemical formula")

        return cls(
            name=format_chemical_name(data.get("name")),
            symbol=format_chemical_name(data.get("symbol")),
            chemical_formula=chemical_formula,
            formula_source=formula_source,
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        raise NotImplementedError()


class MinedData(BaseModel):
    material: Material
    data: Dict[str, Any]
    element_idx: List[str]
    origin_data: List[Dict[str, Any]] = list()

    @property
    def name(
        self,
    ) -> str:
        return self.material.name

    @property
    def symbol(
        self,
    ) -> str:
        return self.material.symbol

    @property
    def chemical_formula(
        self,
    ) -> str:
        return self.material.chemical_formula

    @property
    def clean_chemical_formula(
        self,
    ) -> str:
        return self.material.clean_chemical_formula

    @property
    def formula_source(
        self,
    ) -> str:
        return self.material.formula_source

    def _to_string(self, print_origin_data=False) -> str:
        string = (
            f"Name : {self.name}\n"
            f"Symbol : {self.symbol}\n"
            f"Chemical formula : {self.chemical_formula}\n"
            f"Data :\n{pprint.pformat(self.data, sort_dicts=False)}"
        )
        if print_origin_data:
            string += (
                f"\nOrigin data:\n{pprint.pformat(self.origin_data, sort_dicts=False)}"
            )
        return string

    def print(self, print_origin_data=False) -> None:
        print(self._to_string(print_origin_data))

    def is_equal(self, other: object) -> bool:  # before : isequal_meta
        return self.material.is_equal(other.material)

    def concatenate(self, others: object, overwrite: bool = False) -> None:
        self.material.concatenate(others.material)
        for key, value in others.data.items():
            if (not overwrite) and (key in self.data):
                idx = 1
                new_key = f"{key}_{idx}"
                while new_key in self.data:  # HAVE to fix.
                    idx + 1
                    new_key = f"{key}_{idx}"
                self.data[new_key] = value
            else:
                self.data[key] = value
        self.element_idx.extend(others.element_idx)
        self.origin_data.extend(others.origin_data)

    def to_dict(
        self,
    ) -> Dict[str, Any]:
        raise NotImplementedError()

    def to_json(self, filepath) -> Dict[str, Any]:
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def from_element(
        cls,
    ):
        return cls()

    @classmethod
    def from_data(
        cls,
        data: Dict[str, Any],
        formula_source: str = None,
        element_idx: Optional[List[str]] = None,
    ):
        if "meta" not in data:
            raise KeyError('data must include key "meta"')

        if not element_idx:
            element_idx = list()
        elif not isinstance(element_idx, list):
            element_idx = [str(element_idx)]

        return cls(
            material=Material.from_data(data["meta"], formula_source=formula_source),
            data={key: value for key, value in data.items() if key != "meta"},
            element_idx=element_idx,
            origin_data=[data],
        )

    def from_dict(
        cls,
        data: Dict[str, Any],
    ):
        raise NotImplementedError()

    @classmethod
    def from_json(cls, filepath):
        with open(filepath) as f:
            data = json.load(f)
        return cls.from_dict(data)


class Results(Sequence, BaseModel):
    results: List[MinedData]
    matching_dict: Dict[int, Any]

    def __getitem__(self, idx: int):
        return self.results[idx]

    def __len__(
        self,
    ) -> int:
        return len(self.results)

    def _to_string(self, print_origin_data=False) -> str:
        string = ""
        for data in self.results:
            string += data._to_string(print_origin_data)
            string += "\n" + "-" * 80 + "\n"
        return string

    def print(self, print_origin_data=False) -> None:
        print(self._to_string(print_origin_data))

    def append(self, data: MinedData, idx):  # before: categorize_by_equality
        for jdx, value in enumerate(self.results):
            if jdx not in self.matching_dict.keys():
                self.matching_dict[jdx] = []
            if value.is_equal(data):
                value.concatenate(data)
                self.matching_dict[jdx].append(idx)
                return
        self.results.append(data)

    def to_dict(
        self,
    ) -> Dict[str, Any]:
        raise NotImplementedError()

    def to_json(self, filepath) -> Dict[str, Any]:
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def from_dict(
        cls,
    ):
        raise NotImplementedError()

    @classmethod
    def from_json(cls, filepath):
        with open(filepath) as f:
            data = json.load(f)
        return cls.from_dict(data)

    @classmethod
    def empty(
        cls,
    ):
        return cls(results=list(), matching_dict=dict())
import numpy as np
from collections import defaultdict
from typing import Any, List, Dict, Optional, Set
import json
from pydantic import BaseModel
from collections.abc import Sequence

from llm_miner.meta_collector import Results, MinedData, Material
from llm_miner.meta_collector.utils import format_chemical_formula


class CsdData(BaseModel):
    material: Material
    data: Dict[str, Any]
    matched_idx: List[int] = list()
    element_idx: list = list()
    origin_data: List[Any] = list()

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    @property
    def num_matched(
        self,
    ) -> int:
        return len(self.matched_idx)

    @property
    def chemical_formula(
        self,
    ) -> str:  # FIXME
        return self.material.chemical_formula

    # @property
    # def clean_chemical_formula(
    #     self,
    # ) -> str:
    #     return self.material.clean_chemical_formula

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
    def synonyms(
        self,
    ) -> str:
        return self.material.synonyms

    def isequal_formula(self, mined_data: MinedData) -> bool:  # FIXME
        csd_formula = self.chemical_formula
        mined_formula = mined_data.chemical_formula
        return csd_formula == mined_formula

    def isequal_lattice(self, mined_data: MinedData, threshold=0.01) -> bool:  # FIXME
        try:
            csd_lattice = self.data["lattice parameters"][0]["value"]
            organized_lattice = mined_data.data["lattice parameters"][0]["value"]
        except (KeyError, IndexError):
            return False

        order_ = ["a", "b", "c", "alpha", "beta", "gamma"]
        csd_lattice = np.array([csd_lattice[item] for item in order_])
        tmp_lattice = []
        for item in order_:
            if item not in organized_lattice.keys():
                if item in ["alpha", "beta", "gamma"]:
                    value = 90.0
                elif item in ["b", "c"]:
                    value = organized_lattice["a"]
                else:
                    return False

            else:
                value = organized_lattice[item]

            if not value and item in ["alpha", "beta", "gamma"]:
                value = 90.0
            elif not value and item in ["b", "c"]:
                value = organized_lattice["a"]
            elif not value and item in ["a"]:
                return False

            if value=="-" and item in ["alpha", "beta", "gamma"]:
                value = 90.0
            elif value=="-" and item in ["b", "c"]:
                value = organized_lattice["a"]
            elif value=="-" and item in ["a"]:
                return False

            if isinstance(value, str):
                if value=="= a":
                    value = organized_lattice["a"]
                if "(" in value:
                    value = value[: value.index("(")]
                if "[" in value:
                    value = value[: value.index("[")]

                if "±" in value:
                    value = value[: value.index("±")]

                # if "x" in value:
                #     return False
                value = value.replace("°", "")
                value = value.replace(",", ".")
                value = value.replace("⊡", ".")
                value = value.replace("\'", "")
                value = value.replace("\u2009", "")
                value = value.replace("\u202f", "")
                value = value.replace("∼", "")
                value = value.replace("/", "")
                value = value.replace(">", "")
                value = value.replace(")", "")
                value = value.replace("]", "")
                if "to" in value:
                    value = str(np.mean(np.array(value.split("to")).astype("float")))
                if "-" in value:
                    value = str(np.mean(np.array(value.split("-")).astype("float")))
                value = value.strip().replace(" ", ".")
                parts = value.split(".")
                value = parts[0]+"."+"".join(parts[1:])
                if value=="." and item in ["alpha", "beta", "gamma"]:
                    value = 90.0

                value = float(value)
            tmp_lattice.append(value)
        organized_lattice = np.array(tmp_lattice)

        diff = organized_lattice - csd_lattice
        return np.all(np.abs(diff) < threshold)

    def match_formula(self, results: Results):  # before: isequal_formula
        self.clear()
        for idx, mined_data in enumerate(results):
            if self.isequal_formula(mined_data):
                self.matched_idx.append(idx)

    def match_lattice(
        self,
        results: Results,
        includes: Optional[list] = None,
        excludes: Optional[list] = None,
    ) -> None:  # before: isequal_formula
        self.clear()
        if not excludes:
            excludes = []
        if not includes:
            includes = [i for i in range(len(results)) if i not in excludes]

        for idx, mined_data in enumerate(results):
            if idx not in includes:
                continue
            elif self.isequal_lattice(mined_data):  # FIXME
                self.matched_idx.append(idx)

    def clear(self) -> None:
        self.matched_idx = list()

    def format_data(self):
        add_condition_l = ['crystal system', 'lattice parameters', 'cell volume', 'density', 'color']
        for prop in add_condition_l:
            tmp = []
            for jtem in self.data[prop]:
                jtem['condition'] = ''
                tmp.append(jtem)
            if prop == "color":
                self.data['material color'] = tmp
                del self.data['color']
            else:
                self.data[prop] = tmp

    def concatenate(self, mined_data: MinedData):  # before : concatenate_csd
        bring_condition_l = ['crystal system', 'lattice parameters', 'cell volume', 'density', 'material color']
        for prop in bring_condition_l:
            cond = None
            try:
                cond = mined_data.data[prop][0]['condition']
            except Exception:
                continue
            if cond:
                self.data[prop][0]['condition'] = cond

        
        mined_data.material.refcode = self.material.refcode
        mined_data.material.synonyms = self.material.synonyms
        mined_data.material.formula_source = "csd"
        mined_data.material.is_general = self.material.is_general
        mined_data.data = {**mined_data.data, **self.data}

    def to_dict(
        self,
    ) -> Dict[str, Any]:
        return {
            "material": self.material.to_dict(),
            "data": self.data,
            "element_idx": self.element_idx,
            "origin_data": self.origin_data,
            "matched_idx": self.matched_idx,
        }

    def to_json(self, filepath) -> Dict[str, Any]:
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def from_data(
        cls,
        data: Dict[str, Any],
    ):
        if "meta" not in data:
            raise KeyError('data must include key "meta"')
        material = Material.from_data(data["meta"], formula_source="CSD", refcode=data["refcode"][0]['value'])
        return cls(
            material=material,
            data={key: value for key, value in data.items() if key not in ["meta", "refcode"]},
            matched_idx=list(),
            origin_data=[data],
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> object:
        return cls(
            material=Material.from_dict(data["material"]),
            data=data["data"],
            element_idx=data["element_idx"],
            origin_data=data["origin_data"],
            matched_idx=data["matched_idx"],
        )

    @classmethod
    def from_json(cls, filepath):
        with open(filepath) as f:
            data = json.load(f)
        return cls.from_dict(data)


class CsdCollector(Sequence, BaseModel):
    list_csd: List[CsdData]
    matching_dict: Dict[int, Set[int]] = defaultdict(set)

    def __getitem__(self, index) -> CsdData:
        return self.list_csd[index]

    def __len__(
        self,
    ) -> int:
        return len(self.list_csd)

    def run(
        self,
        results: Results,
    ):  # results에 CSD를 통합하는 형태.
        self.clear()
        self.match(results)
        self.concatenate(results)

    def clear(self) -> None:
        self.matching_dict = defaultdict(set)
        for csd in self.list_csd:
            csd.matched_idx.clear()

    def match(self, results: Results) -> None:
        """
        # 방침.
        chemical formula를 먼저 체크해서 1개이면 그대로 끝.
        2개>이거나 0개면 --> lattice parameter 매칭 진행
        1개이면 그대로 끝.
        2개>이거나 오류니까 그냥 패스.
        0개면 > meta material 추가.

        ** mined result가 2개 이상 합쳐지는지 체크하고 있는데, 이상하면 지우셔도 됩니다. (matching_dict랑 같ㅇ ㅣ지우시면 됨.)
        """
        for i, csd_data in enumerate(self.list_csd):  # 1. formula matching
            csd_data.match_formula(results)
            if csd_data.num_matched >= 2:  # 2. lattice matching for num_matched > 2
                csd_data.match_lattice(results, includes=csd_data.matched_idx)

            if csd_data.num_matched == 1:
            # for m_idx in csd_data.matched_idx:  # 3. matched dict (formula & lattice)
                m_idx = csd_data.matched_idx[0]
                self.matching_dict[m_idx].add(i)

        for key, value in self.matching_dict.items():
            if len(value) >= 2:
                for item in value:
                    self.list_csd[item].clear()
                self.matching_dict[key] = set()
                # raise ValueError("Number of matched material > 1", self.matching_dict)
        matched_list = list(self.matching_dict.keys())  # 4. make first_draft list

        for i, csd_data in enumerate(
            self.list_csd
        ):  # 5. lattice matching for num_matched == 0
            if csd_data.num_matched != 0:
                continue
            csd_data.match_lattice(results, excludes=matched_list)
            if csd_data.num_matched == 1:
                m_idx = csd_data.matched_idx[0]
                self.matching_dict[m_idx].add(i)
                # for m_idx in csd_data.matched_idx:
                    # self.matching_dict[m_idx].add(i)

        for key, value in self.matching_dict.items():
            if len(value) > 2:
                for item in value:
                    self.list_csd[item].clear()
                self.matching_dict[key] = set()
                # raise ValueError("Number of matched material > 1")

    def concatenate(self, results: Results):
        for csd_data in self.list_csd:
            # new_mined_data = MinedData.from_data(csd_data.data)  # FIXME <- 필히 수정 바람.
            if csd_data.num_matched == 1:
                m_idx = csd_data.matched_idx[0]
                csd_data.format_data()
                csd_data.concatenate(results[m_idx])
            elif csd_data.num_matched == 0:
                results.results.append(csd_data)
            else:
                pass

    def to_dict(
        cls,
    ):
        raise NotImplementedError()

    def to_json(
        cls,
    ):
        raise NotImplementedError()

    @classmethod
    def from_dict(cls, data) -> object:
        list_csd = [CsdData.from_data(d) for d in data]
        return cls(list_csd=list_csd)

    @classmethod
    def from_json(cls, filepath):
        with open(filepath) as f:
            data = json.load(f)
        return cls.from_dict(data)

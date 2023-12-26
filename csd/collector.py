from collections import defaultdict
from typing import Any, List, Dict, Optional
import json
from pydantic import BaseModel
from llm_miner.meta_collector import Results, MinedData


# 저도 여기 급하게 짜느라 이상할 수 있으니 편하신 대로 바꾸십쇼
# 최종적으로 Results를 업데이트 하게 만드시면 됩니다.
# 끝.


class CsdData(BaseModel):
    # data: 
    matched_idx: List[int] = list()
    # 형식을 제가 몰라서 맞춰서 바꿔주십쇼
    
    @property
    def num_mached(
        self,
    ) -> int:
        return len(self.matched_idx)

    def match_formula(self, results: Results):  # before: isequal_formula
        self.clear()
        for idx, mined_data in enumerate(results):
            if isequal_formula(mined_data):  # FIXME
                self.matched_list.append(idx)

    def match_lattice(
        self,
        results: Results,
        includes: Optional[list] = None,
        excludes: Optional[list] = None,
    ):  # before: isequal_formula
        self.clear()
        if not excludes:
            excludes = []
        if not includes:
            includes = [i for i in range(len(results)) if i not in excludes]

        for idx, mined_data in enumerate(results):
            if idx not in includes:
                continue
            elif isequal_lattice(mined_data):  # FIXME
                self.matched_list.append(idx)

    def clear(self) -> None:
        self.matched_idx = list()

    def concatenate(self, mined_data: MinedData):  # before : concatenate_csd
        raise NotImplementedError()


class CsdCollector(BaseModel):
    list_csd: List[CsdData]
    matching_dict: Dict[int, List[int]] = defaultdict(list)

    def run(
        self,
        results: Results,
    ):  # results에 CSD를 통합하는 형태.
        self.match(results)
        self.concatenate()

    def match(self, results):
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
            if csd_data.num_matched > 2:  # 2. lattice matching for num_matched > 2
                csd_data.match_lattice(results, includes=csd_data.matched_idx)

            for m_idx in csd_data.matched_idx:  # 3. matched dict (formula & lattice)
                self.matching_dict[m_idx].append(i)

        for value in self.matching_dict.values():
            if len(value) > 2:
                raise ValueError("Number of matched material > 1")
        matched_list = list(self.matching_dict.keys())  # 4. make first_draft list

        for i, csd_data in self.list_csd:  # 5. lattice matching for num_matched == 0
            if csd_data.num_matched != 0:
                continue
            csd_data.match_lattice(results, excludes=matched_list)
            if csd_data.num_matched == 1:
                for m_idx in csd_data.matched_idx:
                    self.matching_dict[m_idx].append(i)

        for value in self.matching_dict.values():
            if len(value) > 2:
                raise ValueError("Number of matched material > 1")

    def concatenate(self, results):
        for csd_data in self.list_csd:
            new_mined_data = MinedData(**csd_data)  # FIXME <- 필히 수정 바람.

            if csd_data.num_mached == 1:
                m_idx = csd_data.matched_idx[0]
                results[m_idx].concatenate(new_mined_data)
            elif csd_data.num_matched == 0:
                results.append(new_mined_data)
            else:
                pass

    @classmethod
    def from_file(cls, filepath) -> object:
        with open(filepath, "r") as f:
            data = json.load(f)

        list_csd = [CsdData(d) for d in data]

        return cls(list_csd=list_csd)

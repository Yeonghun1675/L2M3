from collections import namedtuple
import warnings
import json
from typing import List, Any, Dict, Union, Iterable
from pydantic import BaseModel
from pathlib import Path

from llm_miner.schema import Paragraph, Elements
from llm_miner.parser import parser_dict, Metadata, BaseParser
from llm_miner.parser.utils import publisher_finder
from llm_miner.utils import merge_para_by_token
from llm_miner.error import ReaderError, ParserError
from llm_miner.config import config
from llm_miner.meta_collector import MetaCollector, Results

warnings.filterwarnings("ignore", category=UserWarning, module="bs4")


class JournalReader(BaseModel):
    filepath: Path
    publisher: str
    elements: Elements
    cln_elements: Elements = Elements.empty()
    result: Results = Results.empty()
    # result: Results = []
    metadata: Metadata

    @property
    def filename(self):
        return self.filepath.name.strip()

    @property
    def doi(self):
        if isinstance(self.metadata.doi, str):
            return self.metadata.doi.strip()
        return self.metadata.doi

    @property
    def title(self):
        if isinstance(self.metadata.title, str):
            return self.metadata.title.strip()
        return self.metadata.title

    @property
    def url(self):
        return f"https://doi.org/{self.doi}"

    def get_tables(self) -> List[Paragraph]:
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

    def get_idx(self, idx: Union[int, Iterable[int]]) -> Paragraph:
        if isinstance(idx, int):
            for element in self.elements:
                if int(element.idx) == idx:
                    return element
            raise IndexError(f"There are no idx {idx} in elements.")
        else:
            ls_para = [self.get_idx(i).copy() for i in idx]
            b_para = ls_para[0]
            for para in ls_para[1:]:
                b_para.merge(para, merge_idx=True)
            return b_para

    def to_dict(
        self,
    ) -> Dict[str, Any]:
        return {
            "filepath": str(self.filepath),
            "publisher": self.publisher,
            "elements": self.elements.to_dict(),
            "cln_elements": self.cln_elements.to_dict(),
            "metadata": self.metadata.to_dict(),
            "result": self.result.to_dict(),
        }

    def to_json(self, filepath):
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f)

    def reconstruct(self, model_name: str = "gpt-4") -> None:
        if self.cln_elements:  # clear cln_elements
            self.cln_elements = Elements.empty()

        merge_para_by_token(
            ls_para=self.elements.get_synthesis_conditions(),
            classification="synthesis condition",
            max_tokens=config["input_max_tokens_synthesis"],
            model_name=model_name,
            elements=self.cln_elements,
        )

        merge_para_by_token(
            ls_para=self.elements.get_properties(),
            classification="property",
            max_tokens=config["input_max_tokens_property"],
            model_name=model_name,
            elements=self.cln_elements,
        )

        for table in self.elements.get_tables():
            self.cln_elements.append(table.copy())

        for figure in self.elements.get_figures():
            self.cln_elements.append(figure.copy())

    @classmethod
    def from_file(cls, filepath: str, publisher: str = None):
        if publisher is None:
            raise NotImplementedError("publisher finder is not implemented.")
            # publisher = publisher_finder(filepath)

        publisher = publisher.lower()
        if publisher not in parser_dict:
            raise ReaderError(
                f"publisher must be one of [`acs`, `rsc`, `elsevier`, `springer], not {publisher}"
            )

        parser: BaseParser = parser_dict[publisher]
        try:
            file_bs = parser.open_file(filepath)
            elements = parser.parsing(file_bs)
            metadata = parser.get_metadata(file_bs)
        except Exception as e:
            raise ParserError(e)

        return cls(
            filepath=Path(filepath),
            publisher=publisher,
            elements=Elements(elements=elements),
            metadata=metadata,
        )

    @classmethod
    def from_dict(cls, data):
        if "cln_elements" in data:
            cln_elements = Elements.from_dict(data["cln_elements"])
        else:
            cln_elements = Elements.empty()

        if "result" in data:
            result = Results.from_dict(data["result"])
        else:
            result = Results.empty()

        return cls(
            filepath=Path(data["filepath"]),
            publisher=data["publisher"],
            elements=Elements.from_dict(data["elements"]),
            cln_elements=cln_elements,
            result=result,
            metadata=Metadata.from_dict(data["metadata"]),
        )

    @classmethod
    def from_json(cls, filepath):
        with open(filepath) as f:
            data = json.load(f)
        return cls.from_dict(data)

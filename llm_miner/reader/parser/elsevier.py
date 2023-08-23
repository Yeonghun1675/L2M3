from typing import List
from bs4 import BeautifulSoup
from llm_miner.reader.parser.base import BaseParser, Paragraph, Metadata


class ElsevierParser(BaseParser):
    suffix: str = '.xml'
    parser: str = 'lxml'
    para_tags: List[str] = ['ce:para', 'ce:section-title', 'ce:simple-para']
    table_tags: List[str] = ['ce:table']
    figure_tags: List[str] = ['ce:figure']

    @classmethod
    def open_file(cls, filepath: str):
        with open(filepath, 'r', encoding='UTF-8') as f:
            data = f.read()
        return BeautifulSoup(data, cls.parser)
        
    def _is_para(cls, element):
        try:
            parent_name = element.parent.name
        except AttributeError:
            return False
        else:
            if parent_name in ["ce:acknowledgement", "ce:acknowledgment", "ce:legend", "ce:bibliography", 'ce:keywords', "ce:caption"]:
                return False
            else:
                return True
    
    @classmethod
    def parsing(cls, file_bs):
        elements = []
        for element in file_bs(cls.all_tags):
            if element.name in cls.table_tags:
                type_ = 'table'
            elif elements.name in cls.figure_tags:
                type_ = 'figure'
            elif element.name in cls.para_tags and cls._is_para(element):
                type_ = 'text'
                for tags in element(['ce:cross-refs', 'ce:cross-ref']): # extract crossref
                    tags.extract()
            else:
                continue

            data = Paragraph(
                idx = len(elements) + 1,
                type = type_,
                content = element,
            )
            elements.append(data)
        return elements
    
    @classmethod
    def get_metadata(cls, file_bs):
        try:
            doi = file_bs.find("dc:identifier").text.replace("doi:", "")
        except AttributeError:
            pass
        try:
            title = file_bs.find("dc:title").text.strip()
        except AttributeError:
            pass
        try:
            journal = file_bs.find('prism:publisher').text
        except AttributeError:
            pass
        try:
            date = file_bs.find("prism:coverdate").text
            date = ".".join(date.split("-")[:-1])
        except AttributeError:
            pass
        try:
            author_list = [creator.text for creator in file_bs.find_all("dc:creator")]
        except AttributeError:
            pass

        return Metadata(
            doi=doi,
            title=title,
            journal=journal,
            date=date,
            author_list=author_list,
        )
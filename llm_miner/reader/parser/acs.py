from typing import List
from bs4 import BeautifulSoup
from llm_miner.reader.parser.base import BaseParser, Paragraph, Metadata


class ACSParser(BaseParser):
    suffix: str = '.xml'
    parser: str = 'lxml'
    para_tags: List[str] = ['p', 'title']
    table_tags: List[str] = ['table-wrap']
    figure_tags: List[str] = ['fig']

    @classmethod
    def open_file(cls, filepath: str):
        with open(filepath, 'r', encoding='UTF-8') as f:
            data = f.read()
        return BeautifulSoup(data, cls.parser)
    
    @classmethod
    def parsing(cls, file_bs) -> List[Paragraph]:
        elements = []
        for element in file_bs(cls.all_tags()):
            if element.name in cls.table_tags:
                type_ = 'table'
            elif element.name in cls.figure_tags:
                type_ = 'figure'
            elif element.name in cls.para_tags and cls._is_para(element):
                type_ = 'text'
                for tags in element(['xref', 'named-content', 'fig', 'table-wrap']):
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
    def _is_para(cls, element):
        try:
            parent_name = element.parent.name
        except AttributeError:
            return False
        else:
            if parent_name in ["caption", "table-wrap-foot", "ack", "fn"]:
                return False
        if "content-type" in element.attrs.keys():
            return False
        else:
            return True
    
    @classmethod
    def get_metadata(cls, file_bs) -> Metadata:
        try:
            doi = file_bs.find('article-id', attrs={'pub-id-type': 'doi'}).text
        except AttributeError:
            doi = None
        try:
            title = file_bs.find('title-group').text
        except AttributeError:
            title = None
        try:
            date_tag = file_bs.find(['pub-date', 'date'])
            year = date_tag.find('year').text
            month = date_tag.find('month').text.zfill(2)
            date = f"{year}.{month}"
        except AttributeError:
            date = None
        try:
            journal = file_bs.find('publisher-name').text
        except AttributeError:
            journal = None
        try:
            author_list = [creator.find('name').text.strip() for creator in file_bs.find_all("contrib")]
        except AttributeError:
            author_list = None

        return Metadata(
            doi=doi,
            title=title,
            journal=journal,
            date=date,
            author_list=author_list,
        )
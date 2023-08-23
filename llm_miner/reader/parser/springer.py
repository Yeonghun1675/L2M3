from typing import List
from bs4 import BeautifulSoup
from llm_miner.reader.parser.base import BaseParser, Paragraph, Metadata


class SpringerParser(BaseParser):
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
    def parsing(cls, file_bs):
        elements = []
        for element in file_bs(cls.all_tags):
            if element.name in cls.table_tags:
                type_ = 'table'
            elif element.name in cls.figure_tags:
                type_ = 'figure'
            elif element.name in cls.para_tags and cls._is_para(element):
                type_ = 'text'
                for tags in element(['fig', 'table-wrap']):
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
            
    def _is_para(cls, element):
        if element.text.startswith("!ENTITY"):
            return False
        try:
            parent_name = element.parent.name
        except AttributeError:
            return False
        else:
            if parent_name in ["notes", "td", "caption", "fig", "th", "table-wrap-foot", "ack", "kwd-group", "ref-list"]:
                return False
        return True
    
    @classmethod
    def get_metadata(cls, file_bs):
        try:
            doi = file_bs.find('article-id', attrs={'pub-id-type': 'doi'}).text
        except AttributeError:
            pass
        try:
            title = file_bs.find('title-group').text
        except AttributeError:
            pass
        try:
            date_tag = file_bs.find(['pub-date', 'date'])
            year = date_tag.find('year').text
            month = date_tag.find('month').text.zfill(2)
            date = f"{year}.{month}"
        except AttributeError:
            pass
        try:
            journal = file_bs.find('publisher-name').text
        except AttributeError:
            pass
        try:
            author_list = [creator.find('name').text.strip() for creator in file_bs.find_all("contrib")]
        except AttributeError:
            pass

        return Metadata(
            doi=doi,
            title=title,
            journal=journal,
            date=date,
            author_list=author_list,
        )
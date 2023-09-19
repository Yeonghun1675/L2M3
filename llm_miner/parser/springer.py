from typing import List
from bs4 import BeautifulSoup
from llm_miner.schema import Paragraph
from llm_miner.parser.base import BaseParser, Metadata
from llm_miner.parser.utils import clean_text as f_clean


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
    def parsing(cls, file_bs) -> List[Paragraph]:
        elements = []
        title_para = None

        for element in file_bs(cls.all_tags()):
            if element.name in cls.table_tags:
                type_ = 'table'
                clean_text = ''
            elif element.name in cls.figure_tags:
                type_ = 'figure'
                clean_text = f_clean(element.text)
            elif element.name in cls.para_tags and cls._is_para(element):
                type_ = 'text'
                for tags in element(['fig', 'table-wrap']):
                    tags.extract()
                clean_text = f_clean(element.text)
            else:
                continue

            data = Paragraph(
                idx = len(elements) + 1,
                type = type_,
                content = str(element),
                clean_text=clean_text
            )
            
            if title_para and type_ == 'text':
                title_para.merge(data, merge_idx=False)
                data = title_para
                title_para = None
            else:
                elements.append(data)

            if type_ == 'text' and len(clean_text) < 200 and not title_para:
                title_para = data
                
        return elements
            
    @classmethod
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
    def get_metadata(cls, file_bs) -> Metadata:
        try:
            doi = file_bs.find('article-id', attrs={'pub-id-type': 'doi'}).text
        except AttributeError:
            doi = ""
        try:
            title = file_bs.find('title-group').text
        except AttributeError:
            title = ""
        try:
            date_tag = file_bs.find(['pub-date', 'date'])
            year = date_tag.find('year').text
            month = date_tag.find('month').text.zfill(2)
            date = f"{year}.{month}"
        except AttributeError:
            date = ""
        try:
            journal = file_bs.find('publisher-name').text
        except AttributeError:
            journal = ""
        try:
            author_list = [creator.find('name').text.strip() for creator in file_bs.find_all("contrib")]
        except AttributeError:
            author_list = ""

        return Metadata(
            doi=doi,
            title=title,
            journal=journal,
            date=date,
            author_list=author_list,
        )
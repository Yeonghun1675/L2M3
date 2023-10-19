import re
from typing import List, Any, Tuple
from bs4 import BeautifulSoup
from llm_miner.schema import Paragraph
from llm_miner.parser.base import BaseParser, Metadata
from llm_miner.parser.utils import word_find
from llm_miner.parser.utils import clean_text as f_clean


class RSCParser(BaseParser):
    suffix: str = '.html'
    parser: str = 'html.parser'
    para_tags: List[str] = ['p', 'span']
    table_tags: List[str] = ['table']
    figure_tags: List[str] = ['img', 'div']

    @classmethod
    def open_file(cls, filepath: str):
        with open(filepath, 'r', encoding='UTF-8') as f:
            data = f.read()
        return BeautifulSoup(data, cls.parser)
    
    @classmethod
    def parsing(cls, file_bs) -> List[Paragraph]:
        elements = []
        title_para = None

        for element in file_bs.find_all(cls.all_tags()):
            if element.name in cls.table_tags:
                success, element = cls._is_table(element)
                if not success:
                    continue
                type_ = 'table'
                clean_text = ''
            elif element.name in cls.figure_tags:
                if element.name == "div" and word_find(["image_table"], element, 'class'):
                    type_ = 'figure'
                    clean_text = f_clean(element.text)
                else:
                    continue
            elif element.name in cls.para_tags and cls._is_para(element):
                type_ = 'text'
                for tags in element(['a']): # extract a tag
                    tags.extract()
                for tags in element.find_all('span', attrs=['sup_ref']):
                    tags.extract()
                if not element.text:
                    continue
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
    def _is_table(cls, element)-> Tuple[Any]:
        if "class" not in element.attrs.keys():
            return False, None
        
        caption = None
        up = element.find_previous("div")
        if up:
            for _ in range(3):
                if word_find(["table_caption"], up, 'class'):
                    caption = up
                    element.insert(0, caption)  # insert caption in element
                    return True, element
                up = up.find_previous("div")
                if not up:
                    return True, element
        return True, element
            
    @classmethod
    def _is_para(cls, element) -> bool:
        try:
            parent_name = element.parent.name
        except AttributeError:
            return False
        for attr in ['sup_ref', 'bold', 'ref', 'sub_ref', 'italic', 'small_caps']:
            if attr in element.get_attribute_list('class'):
                return False
        if "id" in element.attrs.keys():
            #print (3, element.get_attribute_list('id'), element.text)
            attributes = " ".join(element.get_attribute_list('id'))
            if re.search(r"(^|\s)fn", attributes):    # footnotes
                return True
            else:                                     # fig / citiation / etc
                return False
        if word_find(["btnContainer", "italic", "header_text", 'graphic_title'], element, 'class'):
            return False
        else:
            return True
    
    @classmethod
    def get_metadata(cls, file_bs) -> Metadata:
        author_list = []
        for meta in file_bs.find_all('meta'):
            if not meta.get('name'):
                continue

            name = meta.get('name')
            if (name.find('citation_') != -1 and name != 'citation_reference') or name.find('dc.') != -1:
                tag = meta.get('name').replace('citation_', '').replace('dc.', '')
                text = meta.get('content')
                if tag == 'doi' or tag == 'Identifier':
                    doi = text
                elif tag == 'title' or tag == 'Title':
                    title = text
                elif tag == 'journal_title':
                    journal = text
                elif tag in ['publication_date', 'Date', 'date']:
                    date = text
                elif tag == 'author' or tag == 'Creator':
                    author_list.append(text, )

        return Metadata(
            doi=doi,
            title=title,
            journal=journal,
            date=date,
            author_list=author_list,
        )
from typing import List
import tiktoken
from llm_miner.reader.parser.base import Paragraph, Elements


def num_tokens_from_string(string: str, model: str) -> int:
    """ get number of tokens for OpenAI models
    :param str string: text for input of OpenAI model
    :param str model: name of models
    :returns: Number of tokens
    """
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def merge_para_by_token(
        ls_para: List[Paragraph], 
        classification: str,
        max_tokens: int, 
        model_name: str, 
        elements: Elements
    ) -> Elements:

    total_tokens = 0
    b_para = ls_para[0].copy()
    b_para.classification = classification
    for para in ls_para[1:]:
        n_tokens = num_tokens_from_string(para.content, model_name)
        if total_tokens + n_tokens <= max_tokens:
            total_tokens += n_tokens
            b_para.merge(para, merge_idx=True)
        else:  # update b_para and make new b_para
            total_tokens = n_tokens
            elements.append(b_para)
            b_para = para.copy()
            b_para.classification = classification
    elements.append(b_para)
    return elements

from typing import List, Optional, Union
import tiktoken
from llm_miner.schema import Paragraph, Elements


def num_tokens_from_string(string: str, model: str) -> int:
    """get number of tokens for OpenAI models
    :param str string: text for input of OpenAI model
    :param str model: name of models
    :returns: Number of tokens
    """
    if model.startswith("ft:gpt-3.5-turbo"):
        model = "gpt-3.5-turbo"
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def merge_para_by_token(
    ls_para: List[Paragraph],
    classification: str,
    max_tokens: Optional[int],
    model_name: str,
    elements: Elements,
) -> Elements:
    total_tokens = 0
    if not ls_para:  # there are no paragraph in ls_para
        return elements

    b_para = ls_para[0].copy()
    b_para.classification = classification
    for para in ls_para[1:]:
        n_tokens = num_tokens_from_string(para.content, model_name)
        if (max_tokens is None) or (total_tokens + n_tokens <= max_tokens):
            total_tokens += n_tokens
            b_para.merge(para, merge_idx=True)
        else:  # update b_para and make new b_para
            total_tokens = n_tokens
            elements.append(b_para)
            b_para = para.copy()
            b_para.classification = classification
    elements.append(b_para)
    return elements

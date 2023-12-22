import re
from typing import List, Union


def format_chemical_name(input_string):
    # Remove HTML tags like <sub>, <italic>, etc., and keep their inner content
    formatted_string = re.sub(r"<[^>]+?>", "", input_string)
    # Replace special characters like · with the appropriate symbol
    formatted_string = formatted_string.replace("⋅", "·")
    return formatted_string


def format_chemical_formula(s):
    # FIXME - 개선 필요
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = re.sub(r"\s*\u22C5\d+\w+", "", s)
    # s = re.sub(r"[()n]", "", s)
    elements = re.findall(r"([A-Z][a-z]?)(\d*)", s)
    new_string = " ".join(
        [f"{elem}{count if count else '1'}" for elem, count in elements]
    )

    """
    new_string = " ".join(sorted(new_string.split(" ")))
    """
    return new_string


def flatten_list_of_dicts(data: List[Union[dict, list]]) -> List[dict]:
    """
    Flattens a list that may contain dictionaries or lists of dictionaries
    into a single list of dictionaries.

    Args:
    data (List[Union[dict, List[dict]]]): The input list containing dictionaries
                                          or lists of dictionaries.

    Returns:
    List[dict]: A flattened list of dictionaries.
    """
    flattened_list = []
    for item in data:
        if isinstance(item, dict):
            flattened_list.append(item)
        elif isinstance(item, list):
            flattened_list.extend(item)
        elif not item:
            continue
        elif item == "Bond & Angle type of table is not target":
            continue
        else:
            raise TypeError(
                f"All items in the list must be dict or list, not {type(item)}: {item}"
            )
    return flattened_list

import regex


def clean_text(text: str):
    """
    - literally cleaning up the text
    """
    # Unicode list
    unicode_space = r"[\u2000-\u2005\u2007\u2008]|\xa0|\n|&nbsp|\t"  # " "
    unicode_waste = r"[\u2006\u2009-\u200F]|\u00ad|\u202f|\u205f"  # ""
    unicode_minus = r"[\u2010-\u2015]|\u2212"  # "-"
    unicode_wave = r"≈|∼"  # "~"
    unicode_quote = r"\u2032|\u201B|\u2019"  # "'"
    unicode_doublequote = r"\u201C|\u201D|\u2033"  # '"'
    unicode_slash = r"\u2215" # "/"
    unicode_rest = r"\u201A"  # ','
    unicode_middle_dot = r"\u2022|\u2024|\u2027|\u00B7"  # "\u22C5"

    # replace unicode stuffs
    text.replace("\n", "")
    text = regex.sub(unicode_space, " ", text)
    text = regex.sub(unicode_waste, "", text)
    text = regex.sub(unicode_minus, "-", text)
    text = regex.sub(unicode_wave, "~", text)
    text = regex.sub(unicode_quote, "'", text)
    text = regex.sub(unicode_doublequote, '"', text)
    text = regex.sub(unicode_slash, "/", text)
    text = regex.sub(unicode_rest, ",", text)
    text = regex.sub(unicode_middle_dot, "\u22C5", text)

    return text


def word_find(words, bs_dict, tag):
    """
    determine whether any word in words is in beautifulsoup_dict[tag]
    """
    try:
        list_a = bs_dict[tag]
    except Exception:
        return False
    for word in words:
        if any(word in s for s in list_a):
            return True
    return False


def word_find_simpled(words, target):
    """
    word_find simplified version to treat non beautifulsoup_dict target
    """
    if not target:
        return False
    for word in words:
        if any(word in s for s in target):
            return True
    return False


def publisher_finder(filepath: str) -> str:
    with open(filepath, 'r', encoding='UTF-8') as f:
            data = f.read()
    
    journal = regex.match(r"\b([Ss]pringer|ACS|RSC|[Ee]lsevier)\b", data)
    if journal:
        return journal
    else:
        raise TypeError('Publisher of paper not in acs, rsc, elsevier, and springer')
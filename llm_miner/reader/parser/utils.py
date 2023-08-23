from bs4 import BeautifulSoup
from chemdataextractor import Document
from collections import namedtuple
import regex


def removeDuplicates(listofElements):
    """
    removes duplicates to make unique list
    """
    uniqueList = []
    for ele in listofElements:
        if ele not in uniqueList:
            uniqueList.append(ele)
    return uniqueList


def tuple_sum(listofElements):
    """
    listofElements --> single string with space inbetween elements
    """
    temp_text = ' '.join(listofElements)
    return temp_text


def is_digit(text):
    """
    determine whether number or not
    """
    # temportal removal of script
    tmp = text[:]
    tmp = regex.sub(r"\[(.+)\]", "", tmp)  # subscript
    tmp = regex.sub(r"`(.+)`", "", tmp)  # superscript

    # see if it can be converted to float
    try:
        tmp = float(tmp)
    except ValueError:
        return False
    return True


def clean_text(text):
    """
    - literally cleaning up the text
    - function from Y.H. KIM
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
    end_punctuation_marks = [".", "!", "?"]

    # remove end punction marks
    if text[-1] in end_punctuation_marks:
        text = text[:-1]

    # modify i.e., e.g., and vs.
    text = regex.sub(r"i\.e\.(?=,|\s)", "that is", text)  # remove i.e.
    text = regex.sub(r"e\.g\.(?=,|\s)", "for example", text)  # remove e.g.
    text = regex.sub(r"vs\s?\.", 'vs', text)  # change vs. -> vs

    # replace unicode stuffs
    text = regex.sub(unicode_space, " ", text)
    text = regex.sub(unicode_waste, "", text)
    text = regex.sub(unicode_minus, "-", text)
    text = regex.sub(unicode_wave, "~", text)
    text = regex.sub(unicode_quote, "'", text)
    text = regex.sub(unicode_doublequote, '"', text)
    text = regex.sub(unicode_slash, "/", text)
    text = regex.sub(unicode_rest, ",", text)
    text = regex.sub(unicode_middle_dot, "\u22C5", text)

    # delete useless html tag part
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()

    # delete duplicated spaces
    text = " ".join(text.split())
    return text


def is_chemical(text, chemlist):
    """
    determine whether the text is chemical or not
    """
    if Document(text).cems:
        return True

    for item in chemlist:
        if item.find(text) != -1:
            return True
        elif len(item) > 2 and text.find(item) != -1:
            return True
    return False


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


def chem_percentage(text, Chemlist):
    chem_per = 0
    tmp = re.split('[\s/]+', text)
    for item in tmp:
        if Utils.is_chemical(item, Chemlist):
            chem_per += 1
    return chem_per/len(tmp)


def replace_script(bs_div):
    # pass
    for su in bs_div.find_all(['sub', 'sup', 'ce:sub', 'ce:sup']):
        text_su = su.get_text()
        if not text_su:
            continue
        if su.name in ['sub', 'ce:sub']:
            su.replace_with(f"_{{text_su}}")
        else:
            su.replace_with(f"`{text_su}`")


def replace_math_exp(sentence):
    start = "\documentclass"
    end = "\end{document}"

    while True:
        try:
            s = sentence.index(start)
            e = sentence.index(end)
        except ValueError:
            break
        else:
            if "$$" in sentence[s:e]:
                sentence = sentence[:s] + "(Math Expression)" + sentence[e+len(end):]
            else:
                print("Need Check for Math Expression")
                raise Exception
    return sentence
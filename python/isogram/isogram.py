from collections import Counter
import re


def is_isogram(string):
    s = re.sub(r"[ -]", "", string.lower())
    c = Counter(s)
    # if sum of values == length of counter, each character only appears once
    return sum(c.values()) == len(c)

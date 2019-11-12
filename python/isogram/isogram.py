from collections import Counter


def is_isogram(string):
    s = string.lower().replace(" ", "").replace("-", "")
    c = Counter(s)
    # if sum of values == length of counter, each character only appears once
    return sum(c.values()) == len(c)

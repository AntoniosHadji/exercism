import re


def word_count(phrase):
    words = re.split(r'[ ,_\t]', phrase)
    result = {}
    for word in words:
        w = str.lower(word).strip("':.\n!&@$%^&")
        if w == '':
            continue
        result[w] = result.get(w, 0) + 1

    return result

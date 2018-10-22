import re


def is_pangram(sentence):
    letters = {}
    for c in re.sub(r'[^a-z]', '', sentence.lower()):
        letters[c] = 1

    return len(letters) == 26

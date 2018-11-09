import re
from collections import Counter


def word_count(phrase):
    words = re.split(r'[ ,_\t\n]', phrase.lower())
    words = [word.strip("':.!&@$%^&") for word in words]
    return Counter([word for word in words if word != ''])

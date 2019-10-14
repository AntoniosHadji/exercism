import string

ALPHABET = string.ascii_lowercase
CIPHER = string.ascii_lowercase[::-1]
"""

In [7]: t = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])

In [8]: "abc".translate(t)
Out[8]: 'zyx'

remove all unwanted characters with strip, then translate
then split into groups of 5

"""


def encode(plain_text):

    # t = str.maketrans(
    #     string.ascii_lowercase + string.digits,
    #     string.ascii_lowercase[::-1] + string.digits,
    # )
    # result = plain_text.lower().replace(" ", "").strip(string.punctuation).translate(t)
    result = ""
    for c in plain_text.lower():

        if c in string.digits:
            result += c

        if c in ALPHABET:
            result += CIPHER[ALPHABET.index(c)]

    result = [result[i : i + 5] for i in range(0, len(result), 5)]
    return " ".join(result)


def decode(ciphered_text):
    result = ""
    for c in ciphered_text.lower():
        if c in string.digits:
            result += c

        if c in ALPHABET:
            result += ALPHABET[CIPHER.index(c)]

    return "".join(result)

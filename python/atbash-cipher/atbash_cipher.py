import string

ALPHABET = string.ascii_lowercase
CIPHER = string.ascii_lowercase[::-1]


def encode(plain_text):

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

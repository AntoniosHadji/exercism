import string


def encode(plain_text):
    result = decode(plain_text)
    result = [result[i : i + 5] for i in range(0, len(result), 5)]
    return " ".join(result)


def decode(ciphered_text):
    t = str.maketrans(
        string.ascii_lowercase[::-1] + string.digits,
        string.ascii_lowercase + string.digits,
        string.whitespace + string.punctuation,
    )
    return ciphered_text.lower().translate(t)

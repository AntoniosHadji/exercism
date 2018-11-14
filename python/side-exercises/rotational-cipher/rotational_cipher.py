import string


def rotate(text, key):
    result = ''
    for c in text:
        if any([c.isspace(), not c.isalpha()]):
            result += c
        else:
            index = (string.ascii_lowercase.index(c.lower()) + key) % 26
            if c.isupper():
                result += string.ascii_lowercase[index].upper()
            else:
                result += string.ascii_lowercase[index]

    return result

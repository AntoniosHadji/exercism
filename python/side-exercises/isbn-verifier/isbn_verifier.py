import re


def verify(isbn):
    isbn = re.sub(r'-', '', isbn)
    if not re.match(r'^\d{9}[0-9X]$', isbn):
        return False

    result = 0
    for i, c in enumerate(isbn):
        if c == 'X':
            result += 10 * (10 - i)
        else:
            result += int(c) * (10 - i)

    return result % 11 == 0

import re


def verify(isbn):
    isbn = re.sub(r'-', '', isbn)
    if not re.match(r'^\d{9}[0-9X]$', isbn):
        return False

    # How to account for X in this code?
    # a = list(isbn)
    # b = list(range(10, 0, -1))
    # return sum([int(x) * y for x, y in zip(a, b)]) % 11 == 0

    if 'X' in isbn:
        result = 10
        isbn = isbn[:-1] + '0'
    else:
        result = 0

    for i, c in enumerate(isbn):
        result += int(c) * (10 - i)

    return result % 11 == 0

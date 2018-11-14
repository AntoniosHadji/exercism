import re


def verify(isbn):
    isbn = isbn.replace('-', '')
    if not re.match(r'^\d{9}[0-9X]$', isbn):
        return False

    a = list(isbn)
    b = list(range(10, 0, -1))

    return sum([
        10 * y if x is 'X' else int(x) * y
        for x, y in zip(a, b)
    ]) % 11 == 0

import re


def verify(isbn):
    isbn = isbn.replace('-', '')
    if not re.match(r'^\d{9}[0-9X]$', isbn):
        return False

    return sum([
        10 * y if x is 'X' else int(x) * y
        for x, y in zip(list(isbn), range(10, 0, -1))
    ]) % 11 == 0

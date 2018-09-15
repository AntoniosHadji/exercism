def reverse(text=''):
    r = list()
    for c in range(len(text)-1, -1, -1):
        r.append(text[c])

    return ''.join(r)

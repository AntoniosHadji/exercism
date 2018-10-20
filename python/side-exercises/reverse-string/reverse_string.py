def reverse(text=''):
    r = [text[i] for i in reversed(range(len(text)))]
    return ''.join(r)

def is_armstrong(number):
    seq = str(number)
    length = len(seq)
    return sum([pow(int(x), length) for x in seq]) == number

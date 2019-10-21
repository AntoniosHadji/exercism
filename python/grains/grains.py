def square(number):
    if not 0 < number <= 64:
        raise ValueError("Number must be greater than zero.")
    return 2 ** (number - 1)


def total(number):
    if not 0 < number <= 64:
        raise ValueError("Number must be greater than zero.")
    if number == 1:
        return number
    return square(number) + total(number - 1)

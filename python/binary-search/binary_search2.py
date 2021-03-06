def binary_search(list_of_numbers, number):
    lo = 0
    hi = len(list_of_numbers)
    while lo < hi:
        index = (lo + hi) // 2
        middle_number = list_of_numbers[index]
        if number == middle_number:
            return index

        if number < middle_number:
            hi = index
            # return binary_search(list_of_numbers[:index], number)
        else:
            lo = index + 1
            # return index + binary_search(list_of_numbers[index:], number)

    if lo == hi:
        raise ValueError("Number not found.")
    try:
        return index
    except NameError:
        raise ValueError("Empty array.")

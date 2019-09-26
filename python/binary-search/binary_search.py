def binary_search(list_of_numbers, number):
    length = len(list_of_numbers)

    if not length:
        raise ValueError("List can not be empty")

    if list_of_numbers[0] == number:
        return 0

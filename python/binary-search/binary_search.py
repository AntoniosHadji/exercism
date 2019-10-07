def binary_search(list_of_numbers, number):
    length = len(list_of_numbers)

    if not length:
        raise ValueError("List can not be empty")
    if length == 1 and number != list_of_numbers[0]:
        raise ValueError("Number not found")

    index = length // 2
    middle_number = list_of_numbers[index]
    if number == middle_number:
        return index

    if number < middle_number:
        return binary_search(list_of_numbers[:index], number)
    else:
        return index + binary_search(list_of_numbers[index:], number)

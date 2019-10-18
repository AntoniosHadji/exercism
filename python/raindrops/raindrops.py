def convert(number):
    """
    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 7 as a factor,
    the result should be the digits of the number.
    """
    data = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
    }

    result = [v for k, v in data.items() if number % k == 0]

    return "".join(result) or str(number)

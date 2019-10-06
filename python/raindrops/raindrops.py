def convert(number):
    """
    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
    """
    result = []
    if not number % 3:
        result.append("Pling")
    if not number % 5:
        result.append("Plang")
    if not number % 7:
        result.append("Plong")

    if result:
        return "".join(result)
    else:
        return str(number)

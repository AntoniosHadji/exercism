def sum_of_multiples(limit, multiples):
    result = []

    for n in range(1, limit):
        for m in multiples:
            if n % m == 0 and n not in result:
                result.append(n)

    return sum(result)

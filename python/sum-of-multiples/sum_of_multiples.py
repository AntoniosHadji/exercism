def sum_of_multiples(limit, multiples):
    result = set()

    for m in multiples:
        result = result.union({n for n in range(m, limit, m) if n % m == 0})

    return sum(result)

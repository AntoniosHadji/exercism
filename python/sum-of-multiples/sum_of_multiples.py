def sum_of_multiples(limit, multiples):
    result = {n for m in multiples for n in range(m, limit, m)}
    return sum(result)

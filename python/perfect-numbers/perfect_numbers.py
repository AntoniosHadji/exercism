import itertools
import math


def classify(n):
    if n < 1:
        raise ValueError("n must be positive non-zero integer")

    factors = set(
        itertools.chain.from_iterable(
            ([i, n // i] for i in range(2, int(math.sqrt(n)) + 1) if n % i == 0)
        )
    )
    factors.add(1)

    if n == 1 or sum(factors) < n:
        return "deficient"
    elif sum(factors) == n:
        return "perfect"
    elif sum(factors) > n:
        return "abundant"

# better community solution
# returns sum of True values (True == 1)
#     return sum(i != j for i, j in zip(strand_a, strand_b))
# expression inside sum is a generator exprssion
# zip does not throw error if not equal length


def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("strands do match in length")

    return len([c for i, c in enumerate(strand_a) if c != strand_b[i]])

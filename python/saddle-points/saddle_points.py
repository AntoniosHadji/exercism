import itertools


def saddle_points(matrix):
    if not matrix:
        return set()

    length = len(matrix[0])
    result = set()

    # enumerate rows of matrix
    for i, row in enumerate(matrix):
        if len(row) != length:
            raise ValueError('irregular matrix')
        # enumerate across columns of row
        for j, col in enumerate(row):
            # if value is max in row, it is potential saddle point
            if col == max(row):
                # loop through column values to find smaller value
                for k in range(len(matrix)):
                    if matrix[k][j] < col:
                        break
                else:
                    # no smaller value found in column, value is saddle point
                    result.add((i, j))
    return result


def saddle_points_v2(matrix):
    if not matrix:
        return set()

    length = len(matrix[0])
    row_set = set()
    col_set = [0] * length
    col_min = [999] * length

    # enumerate rows of matrix
    for i, row in enumerate(matrix):
        if len(row) != length:
            raise ValueError('irregular matrix')
        # enumerate across columns of row
        for j, col in enumerate(row):
            # if value is max in row, it is potential saddle point
            if col == max(row):
                row_set.add((i, j))
            # update column min list as interate through matrix
            if col < col_min[j]:
                col_min[j] = col
                col_set[j] = [(i, j)]
            elif col == col_min[j]:
                col_set[j].append((i, j))

    return row_set.intersection(itertools.chain.from_iterable(col_set))

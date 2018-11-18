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
        for j, cell in enumerate(row):
            # if value is max in row, it is potential saddle point
            if cell == max(row):
                # loop through column values to find smaller value
                for k in range(len(matrix)):
                    if matrix[k][j] < cell:
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
        for j, cell in enumerate(row):
            # if value is max in row, it is potential saddle point
            if cell == max(row):
                row_set.add((i, j))
            # update column min list as interate through matrix
            if cell < col_min[j]:
                col_min[j] = cell
                col_set[j] = [(i, j)]
            elif cell == col_min[j]:
                col_set[j].append((i, j))

    return row_set.intersection(itertools.chain.from_iterable(col_set))


def saddle_points_v3(matrix):
    if not matrix:
        return set()

    length = len(matrix[0])
    row_set = set()
    col_set = set()

    # enumerate rows of matrix
    for i, row in enumerate(matrix):
        if len(row) != length:
            raise ValueError('irregular matrix')
        # if value is max in row, it is potential saddle point
        row_max_index = row.index(max(row))
        row_set.add((i, row_max_index))
        if row.count(max(row)) > 1:
            while True:
                try:
                    row_max_index += 1
                    row_set.add((i, row.index(max(row), row_max_index)))
                except ValueError:
                    break

    transpose = [[matrix[j][i] for j in range(len(matrix))]
                 for i in range(len(matrix[0]))
                 ]
    for i, row in enumerate(transpose):
        col_min_index = row.index(min(row))
        col_set.add((col_min_index, i))
        if row.count(min(row)) > 1:
            while True:
                try:
                    col_min_index += 1
                    col_set.add((row.index(min(row), col_min_index), i))
                except ValueError:
                    break

    return row_set & col_set

import itertools


def saddle_points_v1(matrix):
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


# final submission
def saddle_points_v0(matrix):
    if not matrix:
        return set()

    row_set = list()
    col_set = list()

    # enumerate rows of matrix
    for i, row in enumerate(matrix):
        if len(row) != len(matrix[0]):
            raise ValueError('irregular matrix')
        # if value is max in row, it is potential saddle point
        max_in_row = max(row)
        row_max_index = row.index(max_in_row)
        row_set.append((i, row_max_index))
        # if more than one maximum value, get all
        if row.count(max_in_row) > 1:
            while True:
                try:
                    row_max_index += 1
                    row_set.append((i, row.index(max_in_row, row_max_index)))
                except ValueError:
                    break

    # transpose matrix to operate on columns
    transpose = [list(column) for column in zip(*matrix)]

    for i, row in enumerate(transpose):
        min_in_col = min(row)
        col_min_index = row.index(min_in_col)
        col_set.append((col_min_index, i))
        if row.count(min_in_col) > 1:
            while True:
                try:
                    col_min_index += 1
                    col_set.append((row.index(min_in_col, col_min_index), i))
                except ValueError:
                    break

    # saddle points will be intersection of row maximum and col minimum
    return set(row_set) & set(col_set)

def saddle_points(matrix):
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

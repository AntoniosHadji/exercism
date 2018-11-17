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

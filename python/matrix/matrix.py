class Matrix(object):
    def __init__(self, matrix_string):
        self.m = [list(map(int, e.split(" "))) for e in matrix_string.splitlines()]

    def row(self, index):
        return self.m[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.m]

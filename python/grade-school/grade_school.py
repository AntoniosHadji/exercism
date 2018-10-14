import itertools


class School(object):

    def __init__(self):
        self.data = []

    def add_student(self, name, grade):
        self.data.append((name, grade))

    def roster(self):
        grades = {s[1] for s in self.data}
        # grouped is list of lists
        grouped = [self.grade(g) for g in grades]
        return list(itertools.chain.from_iterable(grouped))

    def grade(self, grade_number):
        return sorted([s[0] for s in self.data if s[1] == grade_number])

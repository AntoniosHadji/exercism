class School(object):

    def __init__(self):
        self.data = []

    def add_student(self, name, grade):
        self.data.append((name, grade))

    def roster(self):
        result = []
        grades = {s[1] for s in self.data}
        for g in grades:
            result += self.grade(g)
        return result

    def grade(self, grade_number):
        return sorted([s[0] for s in self.data if s[1] == grade_number])

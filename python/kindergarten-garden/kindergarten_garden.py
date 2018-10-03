class Garden(object):
    _translate = {'V': 'Violets',
                  'G': 'Grass',
                  'C': 'Clover',
                  'R': 'Radishes'
                  }

    def __init__(self,
                 diagram,
                 students=["Alice", "Bob", "Charlie", "David",
                           "Eve", "Fred", "Ginny", "Harriet",
                           "Ileana", "Joseph", "Kincaid", "Larry"]):
        self._diagram = diagram
        self._students = sorted(students)

    def plants(self, student):
        i = self._students.index(student)
        # index of first plant in row 2
        row2 = self._diagram.index('\n') + 1
        # students plants in row 1
        p = self._diagram[i*2:i*2+2]
        # students plants in row 2
        p += self._diagram[i*2+row2:i*2+row2+2]

        return [self._translate[plant] for plant in p]

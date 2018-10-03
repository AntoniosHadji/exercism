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
        rows = self._diagram.split('\n')
        p = []
        p.append(rows[0][i*2])
        p.append(rows[0][i*2+1])
        p.append(rows[1][i*2])
        p.append(rows[1][i*2+1])

        result = []
        for plant in p:
            result.append(self._translate[plant])
        return result

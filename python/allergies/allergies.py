class Allergies(object):
    test_score = -1
    allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes',
                 'chocolate', 'pollen', 'cats']

    def __init__(self, score):
        self.test_score = score

    def is_allergic_to(self, item):
        if self.test_score == 0:
            return False
        if item in self.lst:
            return True
        else:
            return False

    @property
    def lst(self):
        result = []
        score = self.test_score % 256
        for s in range(7, -1, -1):
            if score & 2**s:
                result.append(self.allergies[s])
        return result

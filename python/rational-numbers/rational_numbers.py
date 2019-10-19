import math


class Rational(object):
    def __init__(self, numer, denom):
        if denom < 0:
            numer *= -1
            denom *= -1
        gcd = math.gcd(int(numer), int(denom))
        self.numer = numer // gcd
        self.denom = denom // gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return "{}/{}".format(self.numer, self.denom)

    def __add__(self, other):
        n = self.numer * other.denom + other.numer * self.denom
        d = self.denom * other.denom
        return Rational(n, d)

    def __sub__(self, other):
        return self.__add__(Rational(-other.numer, other.denom))

    def __mul__(self, other):
        n = self.numer * other.numer
        d = self.denom * other.denom
        return Rational(n, d)

    def __truediv__(self, other):
        return self.__mul__(Rational(other.denom, other.numer))

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(math.pow(self.numer, power), math.pow(self.denom, power))

    def __rpow__(self, base):
        return math.pow(math.pow(base, self.numer), 1 / self.denom)

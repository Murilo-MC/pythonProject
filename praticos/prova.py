class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __repr__(self):
        return str(self.num) + '/' + str(self.den)

    myfraction1 = Fraction(1, 2)
    myfraction2 = Fraction(3, 4)
    print(myfraction1)
    print(myfraction2)

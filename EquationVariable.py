class EquationVariable:
    coef = 1
    exp = 1
    def __init__(self, exp, coef = 1):
        self.exp = exp
        self.coef = coef

    def __add__(self, other):
        if (self.is_equivalence(other)):
            coef = self.coef + other.coef
            return EquationVariable(self.exp, coef)
        return False

    def __sub__(self, other):
        if (self.is_equivalence(other)):
            coef = self.coef - other.coef
            return EquationVariable(self.exp, coef)
        return False

    def __mul__(self, other):
        coef = self.coef
        exp = self.exp
        if (isinstance(other, int)):
            coef *= other
        elif (isinstance(other, EquationVariable)):
            coef *= other.coef
            exp += other.exp
        return EquationVariable(exp, coef)

    def __truediv__(self, other):
        coef = self.coef
        exp = self.exp
        if (isinstance(other, int)):
            coef /= other
        elif (isinstance(other, EquationVariable)):
            coef /= other.coef
            exp -= other.exp
        return EquationVariable(exp, coef)

    def __str__(self):
        return str(self.coef) + "X^" + str(self.exp)

    def is_equivalence(self, other):
        return (self.exp == other.exp)

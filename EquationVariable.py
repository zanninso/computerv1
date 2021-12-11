class EquationVariable:
    coef = 1
    exp = 1
    def __init__(self, exp, coef = 1):
        self.exp = exp
        self.coef = coef

    def __add__(self, other):
        if (self.exp == other.exp):
            coef = self.coef + other.coef
            return EquationVariable(self.exp, coef)
        return False

    def __sub__(self, other):
        if (self.exp == other.exp):
            coef = self.coef - other.coef
            return EquationVariable(self.exp, coef)
        return False

    def __mul__(self, other):
        other_coef = other.coef if isinstance(other, EquationVariable) else other
        other_exp = other.exp if isinstance(other, EquationVariable) else 0
        coef = self.coef * other_coef
        exp = self.exp + other_exp
        return EquationVariable(exp, coef)

    def __truediv__(self, other):
        other_coef = other.coef if isinstance(other, EquationVariable) else other
        other_exp = other.exp if isinstance(other, EquationVariable) else 0
        if (other_coef == 0):
            raise Exception("error: division by 0")
        coef = self.coef / other_coef
        exp = self.exp - other_exp
        return EquationVariable(exp, coef)

    def __str__(self):
        return str(self.coef) + "X^" + str(self.exp)


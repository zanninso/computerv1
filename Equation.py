# from EquationParser import EquationParser
import re
import sys
import operator

class EquationVariable():
    coef = 1
    exp = 1
    def __init__(self, exp, coef = 1):
        self.exp = exp
        self.coef = coef

    def __add__(self, other):
        if (is_equivalence(other)):
            coef = self.coef + other.coef
            return EquationVariable(self.exp, coef)
        return False

    def __sub__(self, other):
        if (is_equivalence(other)):
            coef = self.coef - other.coef
            return EquationVariable(self.exp, coef)
        return False

    def __mul__(self, other):
        coef = self.coef * other.coef
        exp = self.exp + other.exp
        return EquationVariable(exp, coef)

    def __truediv__(self, other):
        if other.coef != 0:
            coef = self.coef / other.coef # be aware /0
            exp = self.exp - other.exp
            return EquationVariable(exp, coef)
        return False

    def is_equivalence(self, other):
        return (self.exp == other.exp)

class Equation:
    equationValid = True
    Right = 1
    Left = 0
    side = Left
    sides_list = [[],[]]
    polynome = []

    def append(self, item):
        if isinstance(item, str):
            if item == '=':
                self.side = self.Right
            else :
                self.sides_list[self.side].append(item)
        elif isinstance(item, EquationVariable):
            self.sides_list[self.side].append(item)


    def execute_mul_div(self):
        ops = { "*": operator.mul, "/": operator.truediv }
        for side in range(2):
            operators = []
            side_len = len(self.sides_list[side])

            for i in range(side_len)
                item = self.sides_list[self.Left][i]
                if isinstance(item, str) and (item == '*' or item == '/'):
                    operators.appendleft(item)
            
            for i in operators
                opr = self.sides_list[side][i]
                left_opr = self.sides_list[side][i - 1]
                right_opr = self.sides_list[side][i + 1]
                self.sides_list[side][i - 1] = ops[opr](left_opr, right_opr)
                del self.sides_list[side].[i:(i + 2)]
    
    def get_degrees():
        degrees = set()
        for side in range(2):
            side_len = len(self.sides_list[side])
            for i in range(side_len)
                item = self.sides_list[self.Left][i]
                if isinstance(item, EquationVariable):
                    degrees.add(item.exp)
        degrees = list(degrees)

        for degre in degrees:
            self.polynome.append(EquationVariable(degre, 0))
        return degrees
        
    def reduce_polynome(self):
        degrees = get_degrees()

        for side in range(2):
            side_len = len(self.sides_list[side])
            default_sign = 1 if side == 0 else -1 
            sign = default_sign
            for i in range(side_len):
                item = self.sides_list[self.Left][i]
                if isinstance(item, str) and (item == '-' or item == '+'):
                    sign *= -1 if item == '-' else 1
                elif isinstance(item, EquationVariable):
                    self.polynome[degrees.index(item.exp)] += (item * sign)
                    sign = default_sign
        print(self.polynome)

    # def solve(self):


# from EquationParser import EquationParser
import operator
from EquationVariable import EquationVariable

class Equation:
    equationValid = True
    Right = 1
    Left = 0
    side = Left
    sides_list = [[],[]]
    polynome = []
    __degree = 0
    __has_negative_degree = False
    __solutions = []

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

            for i in range(side_len):
                item = self.sides_list[self.Left][i]
                if isinstance(item, str) and (item == '*' or item == '/'):
                    operators.insert(0, i)

            for i in operators:
                opr = self.sides_list[side][i]
                left_opr = self.sides_list[side][i - 1]
                right_opr = self.sides_list[side][i + 1]
                self.sides_list[side][i - 1] = ops[opr](left_opr, right_opr)
                del self.sides_list[side][i:(i + 2)]
    
    def get_degrees(self):
        degrees = set()
        for side in range(2):
            side_len = len(self.sides_list[side])
            for i in range(side_len):
                item = self.sides_list[self.Left][i]
                if isinstance(item, EquationVariable):
                    degrees.add(item.exp)
        degrees = list(degrees)

        for degre in degrees:
            self.polynome.append(EquationVariable(degre, 0))
        return degrees
    
    def reduce_polynome(self):
        self.execute_mul_div()
        degrees = self.get_degrees()

        for side in range(2):
            side_len = len(self.sides_list[side])
            default_sign = 1 if side == 0 else -1 
            sign = default_sign
            for i in range(side_len):
                item = self.sides_list[side][i]
                if isinstance(item, str) and (item == '-' or item == '+'):
                    sign *= -1 if item == '-' else 1
                elif isinstance(item, EquationVariable):
                    self.polynome[degrees.index(item.exp)] += (item * sign)
                    sign = default_sign

        self.polynome.sort(key = (lambda var: (var.exp)), reverse = True)
        self.__degree = 0 if len(self.polynome) == 0 else self.polynome[0].exp
        self.__has_negative_degree = len(filter(lambda var: (var.exp < 0), self.polynome)) > 0

    def insert_missing_degrees():
        for i in range(self.__degree + 1)
            if (self.polynome[i].exp != self.__degree - i)
                self.polynome.insert(i, EquationVariable(self.__degree - i, 0))
    
    def __str__(self):
        str_polynome = ""
        start = True
        for var in self.polynome:
            if (start == False):
                str_polynome += "+ "
            str_polynome += str(var) + " "
            start = False
        str_polynome += " = 0"

    def __solve_degree1(self):
        n = 1 if len(self.polynome) == 1 else (self.polynome[1].coef * -1)
        self.__solutions.append(n / self.polynome[0].coef)

    def __solve_degree2(self):
        self.insert_missing_degrees()
        a,b,c = self.polynome[0].exp, self.polynome[1].exp, self.polynome[2].exp
        delta = pow(b, 2) - 4 * a * c
        if (delta == 0):
            solution.append(-b / (2 * a))
        elif (delta > 0):
            solution.append((-b + sqrt(deta)) / (2 * a))
            solution.append((-b - sqrt(deta)) / (2 * a))
        elif (delta < 0):
            solution.append(str(-b / (2 * a)) + " + " + str(sqrt(delta) / (2 * a)) + "i")
            solution.append(str(-b / (2 * a)) + " - " + str(sqrt(delta) / (2 * a)) + "i")


    def solve(self):
        if (self.__degree == 0):
            self.__solutions.append("each real number is a solution")

        elif (self.__degree == 1):
            self.__solve_degree1()

        elif (self.__degree == 2):
            self.__solve_degree1()

        else
            self.__solutions.append("The polynomial degree is strictly greater than 2, I can't solve.")

        print("Reduced form:")
        print("Polynomial degree:", self.__degree)
        print("The solution is:")
        for solution in self.__solutions:
            print (solution)



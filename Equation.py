# from EquationParser import EquationParser
import operator
from EquationVariable import EquationVariable
from mathmy import sqrt

class Equation:
    __Right = 1
    __Left = 0
    __side = __Left
    __sides_list = [[],[]]
    __polynome = []
    __degree = 0
    __has_negative_degree = False
    __solutions = []

    def append(self, item):
        if isinstance(item, str):
            if item == '=':
                self.__side = self.__Right
            else :
                self.__sides_list[self.__side].append(item)
        elif isinstance(item, EquationVariable):
            self.__sides_list[self.__side].append(item)


    def execute_mul_div(self):
        ops = { "*": operator.mul, "/": operator.truediv }
        for side in range(2):
            operators = []
            side_len = len(self.__sides_list[side])

            for i in range(side_len):
                item = self.__sides_list[side][i]
                if isinstance(item, str) and (item == '*' or item == '/'):
                    operators.insert(0, i)

            for i in operators:
                opr = self.__sides_list[side][i]
                left_opr = self.__sides_list[side][i - 1]
                right_opr = self.__sides_list[side][i + 1]
                self.__sides_list[side][i - 1] = ops[opr](left_opr, right_opr)
                del self.__sides_list[side][i:(i + 2)]
    
    def get_degrees(self):
        degrees = set()
        for side in range(2):
            side_len = len(self.__sides_list[side])
            for i in range(side_len):
                item = self.__sides_list[self.__Left][i]
                if isinstance(item, EquationVariable):
                    degrees.add(item.exp)
        degrees = list(degrees)

        for degre in degrees:
            self.__polynome.append(EquationVariable(degre, 0))
        return degrees
    
    def reduce_polynome(self):
        self.execute_mul_div()
        degrees = self.get_degrees()

        for side in range(2):
            side_len = len(self.__sides_list[side])
            default_sign = 1 if side == 0 else -1 
            sign = default_sign
            for i in range(side_len):
                item = self.__sides_list[side][i]
                if isinstance(item, str) and (item == '-' or item == '+'):
                    sign *= -1 if item == '-' else 1
                elif isinstance(item, EquationVariable):
                    self.__polynome[degrees.index(item.exp)] += (item * sign)
                    sign = default_sign
        self.__polynome = list(filter(lambda var: (var.coef != 0), self.__polynome))
        self.__polynome.sort(key = (lambda var: (var.exp)), reverse = True)
        self.__degree = 0 if len(self.__polynome) == 0 else self.__polynome[0].exp
        self.__has_negative_degree = len(list(filter(lambda var: (var.exp < 0), self.__polynome))) > 0

    def insert_missing_degrees(self):
        for i in range(self.__degree + 1):
            if (i >= len(self.__polynome) or self.__polynome[i].exp != self.__degree - i):
                self.__polynome.insert(i, EquationVariable(self.__degree - i, 0))
    
    def __str__(self):
        str_polynome = ""
        start = True
        for var in self.__polynome:
            if (start == False):
                str_polynome += "+ "
            str_polynome += str(var) + " "
            start = False
        str_polynome += "= 0"
        return str_polynome

    def __solve_degree1(self):
        self.insert_missing_degrees()
        self.__solutions.append(self.__polynome[1].coef / self.__polynome[0].coef)

    def __solve_degree2(self):
        self.insert_missing_degrees()
        a,b,c = self.__polynome[0].coef, self.__polynome[1].coef, self.__polynome[2].coef
        delta = (b*b) - 4 * a * c
        if (delta == 0):
            self.__solutions.append(-b / (2 * a))
        elif (delta > 0):
            self.__solutions.append((-b - sqrt(delta)) / (2 * a))
            self.__solutions.append((-b + sqrt(delta)) / (2 * a))
        elif (delta < 0):
            r, i = -b / (2 * a), sqrt(delta) / (2 * a)
            self.__solutions.append("{:.6f}".format(r) + " - " + "{:.6f}".format(i) + "i")
            self.__solutions.append("{:.6f}".format(r) + " + " + "{:.6f}".format(i) + "i")

    def solve(self):
        if self.__has_negative_degree:
            raise Exception("negative exponent are not acceptable")

        elif (self.__degree == 0 and len(self.__polynome) > 0):
            self.__solutions.append("there is no solution")
            
        elif (self.__degree == 0):
            self.__solutions.append("each real number is a solution")

        elif (self.__degree == 1):
            self.__solve_degree1()

        elif (self.__degree == 2):
            self.__solve_degree2()

        else:
            self.__solutions.append("The polynomial degree is strictly greater than 2, I can't solve.")

        print("Reduced form:", self)
        print("Polynomial degree:", self.__degree)
        print("The solution is:")
        for s in self.__solutions:
            print (s if isinstance(s, str) else "{:.6f}".format(s))

    def print_equation(self):
        print ("equation:",  end = ' ')
        for var in self.__sides_list[0]:
            print (var,  end = ' ')
        print ('=', end = ' ')
        for var in self.__sides_list[1]:
            print (var,  end = ' ')
        print()

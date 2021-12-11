import re
from Equation import Equation
from EquationVariable import EquationVariable

# don't forget to manage the real numbers.
class EquationParser:
    __equationValid = True
    __expected_types = []
    __newEquation = None
    __itemsPattern = []
    __itemsPattern.append("\d*\.?\d*\s*[Xx]\s*\^\s*[\-\+]?\d+|\d*\.?\d*[Xx]")    # pattern to get the variable with and without exponant
    __itemsPattern.append("\d+\.?\d*")                                    # pattern to get numbers
    __itemsPattern.append("[\+\-\*\/\=]")                                 # pattern to get operators
    __itemsPattern.append("\S+")                                          # pattern to get deffirent from the patterns above
    __sign = 1
    __equal = False

    def parse(self, equation):
        self.__expected_types = ["Variable", "Number", "Sign"]
        self.__equal = False
        if (isinstance(equation, str)):
            tokens = re.findall("|".join(self.__itemsPattern), equation)
            self.__newEquation = Equation()
            for token in tokens:
                for expected_type in self.__expected_types:
                    self.__equationValid = getattr(self, expected_type)(token)
                    if self.__equationValid:
                        break
                if self.__equationValid == False:
                    raise Exception("syntax error: except " + ", ".join(self.__expected_types) + " found: " + token)
            return self.__newEquation
        raise Exception("invalide arg given, except just string")

    def Variable(self, token):
        if re.match(self.__itemsPattern[0], token):
            values = re.split(',', re.sub("\s*[Xx]\s*\^*|\s*]", ',', token))
            coef = (float(values[0]) if values[0] != '' else 1) * self.__sign
            exp = int(values[1]) if values[1] != '' else 1
            self.__newEquation.append(EquationVariable(exp, coef))
            self.__sign = 1
            self.__expected_types = ["Operator"]
            return True
        return False

    def Number(self, token):
        if re.match(self.__itemsPattern[1], token):
            coef = float(token) * self.__sign
            self.__newEquation.append(EquationVariable(0, coef))
            self.__sign = 1
            self.__expected_types = ["Operator"]
            return True
        return False

    def Sign(self, token):
        if re.match("[\-\+]", token):
            self.__sign = 1 if token == '+' else -1
            self.__expected_types = ["Variable", "Number"]
            return True
        return False

    def Operator(self, token):
        if re.match(self.__itemsPattern[2], token):
            if (token == '=' and self.__equal == True):
                raise Exception("syntax error: double equal operator")
            if (token == '='):
                self.__equal = True
            self.__newEquation.append(token)
            self.__expected_types = ["Variable", "Number", "Sign"]
            return True
        return False

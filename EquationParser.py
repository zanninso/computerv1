import re
from Equation import Equation
from EquationVariable import EquationVariable

# don't forget to manage the real numbers.
class EquationParser:
    equationValid = True
    expected_types = ["Variable", "Number", "Sign"]
    newEquation = None
    itemsPattern = []
    
    itemsPattern.append("\d*\.?\d*\s*[Xx]\s*\^\s*\d+|\d*\.?\d*[Xx]")     # pattern to get the variable with and without exponant
    itemsPattern.append("\d+\.?\d*")                                 # pattern to get numbers
    itemsPattern.append("[\+\-\*\/\=]")                         # pattern to get operators
    itemsPattern.append("\S+")                                  # pattern to get deffirent from the patterns above
    sign = 1
    equal = False

    def parse(self, equation):
        if (isinstance(equation, str)):
            tokens = re.findall("|".join(self.itemsPattern), equation)
            self.newEquation = Equation()
            print(tokens) #debug
            for token in tokens:
                print("expected_types:", self.expected_types, "token:", token) #debug
                for expected_type in self.expected_types:
                    self.equationValid = getattr(self, expected_type)(token)
                    if self.equationValid:
                        break
                if self.equationValid == False:
                    print("error")
                    return None
            print("equation good")
            return self.newEquation

    def Variable(self, token):
        if re.match(self.itemsPattern[0], token):
            print("Variable", token)
            values = re.split(',', re.sub("\s*[Xx]\s*\^*|\s*]", ',', token))
            coef = (self.ConvertNum(values[0]) if values[0] != '' else 1) * self.sign
            exp = self.ConvertNum(values[1]) if values[1] != '' else 0
            self.sign = 1
            print(exp, coef) #debug
            self.newEquation.append(EquationVariable(exp, coef))
            self.expected_types = ["Operator"]
            return True
        return False

    def Number(self, token):
        if re.match(self.itemsPattern[1], token):
            print("Number", token) #debug
            coef = self.ConvertNum(token) * self.sign
            self.sign = 1
            self.newEquation.append(EquationVariable(0, coef))
            self.expected_types = ["Operator"]
            return True
        return False

    def Sign(self, token):
        if re.match("[\-\+]", token):
            self.sign = 1 if token == '+' else -1
            print("Sign", token) #debug
            self.expected_types = ["Variable", "Number"]
            return True
        return False

    def Operator(self, token):
        if re.match(self.itemsPattern[2], token):
            print("Operator", token) #debug
            if (token == '=' and self.equal == True):
                print("multipe equal operator")
                return False
            self.equal = (token == '=')
            self.newEquation.append(token)
            self.expected_types = ["Variable", "Number", "Sign"]
            return True
        return False
    
    def ConvertNum(self, num):
        return float(num) if re.search("\.\d*", num) else int(num)

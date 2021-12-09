from EquationParser import *
from EquationVariable import EquationVariable

if re.match("\d+\.\d+", "4.22"):
    print ("float")

equationParser = EquationParser()
eq = equationParser.parse("X+4. * -4x^5   + x^3 - X^3 + X^2 = +3 X^2")
if (eq == None):
    print("error")
else:
    for var in eq.sides_list[0]:
        print (var,  end = ' ')
    print ('=', end = ' ')
    for var in eq.sides_list[1]:
        print (var,  end = ' ')
    print()
eq.reduce_polynome()
eq.print_polynome()

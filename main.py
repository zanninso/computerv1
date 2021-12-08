from EquationParser import *

if re.match("\d+\.\d+", "4.22"):
    print ("float")

eq = EquationParser("X+4. * -4x^5   + x^3 - X^3 + X^2= +3 X^2")

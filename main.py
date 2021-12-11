from EquationParser import *
from EquationVariable import EquationVariable
import sys

if len(sys.argv) == 2:
    try:
        equationParser = EquationParser()
        eq = equationParser.parse(sys.argv[1])
        eq.reduce_polynome()
        eq.solve()
    except Exception as e:
        print(e)
else:
    print("invalid argument should give an equation in one argument")

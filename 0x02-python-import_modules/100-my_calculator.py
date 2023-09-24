#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

options = {"+": add, "-": sub, "*": mul, "/": div}
operator = sys.argv[2]

if operator not in options:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a, b = int(sys.argv[1]), int(sys.argv[3])
result = options[operator](a, b)
print("{} {} {} = {}".format(a, operator, b, result))

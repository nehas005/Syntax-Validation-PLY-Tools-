# main.py
from lexer import lexer
from parser import parser

# TEST code
code = """
def calculate(a, b):
    x = a * (b + 5))
    if (x >= 100):
        return x / 2
    else:
        if (x != 50):
            return 1
var = 999
"""

print("---Python Syntax Validation---")
parser.parse(code, lexer=lexer)



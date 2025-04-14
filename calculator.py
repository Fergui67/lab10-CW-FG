# # https://github.com/Fergui67/lab10-CW-FG.git
# Partner 1: Fernando Guillen
# Partner 2: Cade Wedekind
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math
def square_root(a):
    if a<0:
        raise ValueError
    else:
        return math.sqrt(a)
def hypotenuse(a,b):
    math.hypot(a,b)
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        return "Error: Logarithm base and argument must be positive."
    return math.log(b, a)

def exp(a, b):
    return a ** b

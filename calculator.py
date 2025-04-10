# https://github.com/SuyeshThapa/lab10-ST-STC.git
# Partner 1: Suyesh Thapa
# Partner 2: Suyesh Thapa Clone

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError

    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError

    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError

    return math.log(b, a)

def exp(a, b):
    return a ** b
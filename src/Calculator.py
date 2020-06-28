import math

def addition (a, b):
    return float(a) + float(b)

def subtraction (a,b):
    a = float (a)
    b = float(b)
    c = b - a
    return c

def division (a, b):
    x = float(b) / float(a)
    limited_float = round(x, 9)
    return limited_float

def multiplication (a, b):
    return float(a) * float(b)

def squaring (a):
    return float(a) * float(a)

def squareroot (a):
    x = float(a)
    y = math.sqrt(x)
    limited_float1 = round(y, 8)
    return limited_float1

'''
def squareroot2 (a):
    x = float(a)
    y = math.sqrt(x)
    limited_float1 = round(y, 8)
    return limited_float1
'''

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def rooting(self, a):
        self.result = squareroot(a)
        return self.result
'''

def rooting2(self, a):
        self.result = squareroot2(a)
        return self.result
'''




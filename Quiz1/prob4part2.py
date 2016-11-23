#!/usr/bin/python

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return a * x**2 + b * x + c


# print evalQuadratic(3, 3, -3, 0.618033)

a1 = -4.69
b1 = -4.03
c1 = -4.91
x1 = 2.91
a2 = 3.05
b2 = -8.12
c2 = -4.99
x2 = -5.64


def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    return evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2) 
       

print twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2) # 81.473391


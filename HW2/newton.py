'''
    PIC 16A Homework 2
    Author: Jiayu Li
    UID: 605348766
    Discussion Section: 3B
    Date: 01/26/2023
'''

from math import *

def solve(function, x0, tol):
    f = function(x0)
    # f,fp = function(x0)
    # find the desired value x that is close enough to the root of f(x)
    if abs(f[0]) > tol:
        return solve(function, x0 - f[0]/f[1], tol)
        # return solve(function, x0 - f/fp, tol)
    else:
        return x0
    

# function f(x) = lambda x : x ** 2 - 1
# function’s derivative f'(x) = lambda x : 2 * x 
initial_guess = solve(lambda x : (x ** 2 - 1, 2 * x), 3, 1e-4) # function 1
print(initial_guess)

initial_guess = solve(lambda x : (x ** 2 - 1, 2 * x), -1, 1e-4) # function 2
print(initial_guess)

initial_guess = solve(lambda x : (exp(x) - 1, exp(x)), 1, 1e-4) # function 3
print(initial_guess)

initial_guess = solve(lambda x : (sin(x), cos(x)), 0.5, 1e-4) # function 4
print(initial_guess)


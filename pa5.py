#!/usr/bin/env python
# coding: utf-8

# 0.0.1 Problem 1: GCD

def gcd(a, b):
    
    if b == 0:
        return a
    if a == b:
        return a
    if a < b:
        return gcd(a, b % a)
    if b < a:
        return gcd(b, a % b)
        

# 0.0.2 Problem 2: Directions

def remove_pairs(directions):
    
    turnarounds = {'EW', 'WE', 'NS', 'SN'}

    if len(directions) <= 1:
        return directions

    pair = directions[:2]
    if pair in turnarounds:
        return remove_pairs(directions[2:])
    else:
        return directions[0] + remove_pairs(directions[1:])
        
        
# 0.0.3 Problem 3: Bisection Method

import math

def bisection_root(equation, x1, x2):
    
    if equation(x1) * equation(x2) > 0:
        raise ValueError('Cannot find the root between these values')
    if abs(equation(x1)) < 0.0000001:
        return x1
    if abs(equation(x2)) < 0.0000001:
        return x2
    x = (x1 + x2) / 2
    y = equation(x)
    if (y < 0 and equation(x1) > 0) or (y > 0 and equation(x1) < 0):
        return bisection_root(equation, x, x1)
    elif (y < 0 and equation(x2) > 0) or (y > 0 and equation(x2) < 0):
        return bisection_root(equation, x, x2)
    else:
        raise ValueError('Cannot find a root between these values')

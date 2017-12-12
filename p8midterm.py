#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:57:37 2017

@author: Dustin
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def arith(x):
        total = 0
        length = len(L) - 1
        for z in L:
            total = total + (z * (x**length))
            length = length - 1
        print (total)
        return total
    return arith

L = [1, 2, 3, 4]

general_poly(L)(10)
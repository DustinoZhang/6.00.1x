#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 21:43:16 2017

@author: Dustin
"""
balance = 3329
annualInterestRate = 0.2
MRI = (annualInterestRate/12)
def calcUB (b, mmp):
    return (b - mmp)
def updateB(b, r):
    return (b + (r * b))
def calcYear(pay):
    out = balance
    count = 0
    while count < 12:
        temp = calcUB(out, pay)
        out = updateB(temp, MRI)
        count += 1
    return out    

def guessMMP(guess):
    gb = calcYear(guess)
    loop = True
    while loop:
        if gb == 0:
            loop = False
        elif gb > 0:
            guess += 10
            gb = calcYear(guess)
        elif gb < 0:
            guess -= 10
            gb = calcYear(guess)
    return guess
    
print ("Lowest Payment: " + str(guessMMP(10)))
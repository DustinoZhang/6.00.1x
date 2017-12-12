#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:28:35 2017

@author: Dustin
"""
balance = 3329
annualInterestRate = 0.2
guessP = 10
#high = balance
#low = 0

def calcUB (b, mmp):
    return b - mmp
def updateB(r, ub):
    return ub + (r * ub)


def guessMMP(g):
    tempB = balance
    global guessP
    for x in range(12):
        tempB = updateB(annualInterestRate/12, calcUB(balance, g))
    if tempB == 0:
        return g
    elif tempB > 0:
        g += 10
        return (guessMMP(g))
    elif tempB < 0:
       # high = guessP
      #  guessP = int((guessP + low)/2)
        g -= 10
        return (guessMMP(g))
        
print ("Lowest Payment: " + str(guessMMP(guessP)) )
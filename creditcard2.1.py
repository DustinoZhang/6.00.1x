#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 19:10:00 2017

@author: Dustin
"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def calcMMP (mr, b):
    return mr*b    
def calcUB (b, mmp):
    return b - mmp
def updateB(r, ub):
    return ub + (r * ub)

for x in range(12):
    min = calcMMP(monthlyPaymentRate, balance)
    balance = round(updateB(annualInterestRate/12, calcUB(balance, min)), 2)
print("Remaining balance: " + str(balance))
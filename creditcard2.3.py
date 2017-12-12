#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 23:45:36 2017

@author: Dustin
"""
balance = 320000; annualInterestRate = 0.2
mri = annualInterestRate/12
lower = balance/12
upper = (balance * (1+mri)**12)/12
solidBalance = balance
endBalance = 3
monthlyPayment = 0
while endBalance != 0:
    monthlyPayment = (lower + upper)/2
    balance = solidBalance
    for i in range(12):
        balance = balance - monthlyPayment
        balance = balance + (mri*balance)
    endBalance = balance
    print('Remaining balance: ' + str(round(balance,2)))
    if endBalance > 0:
        lower = monthlyPayment
    elif endBalance < 0:
        upper = monthlyPayment
    endBalance = int(endBalance)
    
print("Lowest Payment: " + str(round(monthlyPayment, 2)))
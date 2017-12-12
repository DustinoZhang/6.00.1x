#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 23:16:29 2017

@author: Dustin
"""

# Paste your code into this box
endBalance = 5
monthlyInterestRate = annualInterestRate/12
solidBalance = balance
monthlyPayment = 0
while(endBalance>0): 
    monthlyPayment+=10
    balance = solidBalance
    for i in range (0, 12):
       balance -= monthlyPayment
       balance +=  (balance*monthlyInterestRate)
       #print('for month ' + str(i+1) + ' the updated balance is: ' + str(balance))
       
    #print('Remaining balance: ' + str(round(balance,2)))
    endBalance = balance

print (monthlyPayment)

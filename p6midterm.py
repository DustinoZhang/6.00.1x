#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:46:54 2017

@author: Dustin
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    overall = {}
    for x in L:
        if not(x in overall.keys()):
            overall[x] = 1
        else:
            overall[x] = overall[x] + 1
    finding = True
    value = 0
    while finding:
        if overall == {}:
            finding = False
            return None
        check = max(overall.keys())
        if(overall[check] % 2 != 0):
            finding = False
            value = check
        else:
            del overall[check]
    return value
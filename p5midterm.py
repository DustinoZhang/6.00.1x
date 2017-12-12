#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:39:26 2017

@author: Dustin
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    new = ""
    vowels = "aeiou"
    for c in s:
        if not(c.lower() in vowels):
            new = new + c
    print (new)

print_without_vowels("deez")
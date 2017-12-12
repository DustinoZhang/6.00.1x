#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:30:24 2017

@author: Dustin
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    tricheck = 1
    count = 2
    if tricheck == k:
        return True
    while k != tricheck and k > tricheck:
        tricheck = tricheck + count
        count += 1
        if k == tricheck:
            return True
    return False
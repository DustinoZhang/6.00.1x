#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:53:07 2017

@author: Dustin
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    inverted = {}
    convalues = []
    conkeys = []
    uniqueindices = {}
    count1 = 0
    track = 0
    #parallel build keys and values
    for x in d.keys():
       if not(d[x] in convalues):
           convalues.append(d[x])
           conkeys.append([x])
           uniqueindices[count1] = d[x]
           count1 += 1    
       else:
           for z in uniqueindices.keys():
               if d[x] == uniqueindices[z]:
                   track = z
           conkeys[track].append(x)
    
    #sorting conkeys elements
    for x in range(len(conkeys)):
        conkeys[x].sort()
        
    #inserting built lists into inverted dic    
    count2 = 0   
    for x in convalues:
        inverted[x] = conkeys[count2] 
        count2 += 1
    
    #sorting new dictionary by keys
    print(inverted)  
    return inverted


x = {0: 1, 2: 1, 3: 3, 6: 3}
d = {1:10, 2:20, 3:30, 4:30}
dict_invert(d)
# nd = {10: [1], 20: [2], 30: [3, 4]}
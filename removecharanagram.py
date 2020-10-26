#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:09:04 2019

@author: aishee
"""
from collections import Counter
def removechar(s1,s2):
    dict1=Counter(s1)
    dict2=Counter(s2)
    print(dict1)
    key1=dict1.keys()
    key2=dict2.keys()
    print(key1)
    count1=len(key1)
    count2=len(key2)
    print(count1)
    set1=set(key1)
    commonKeys = len(set1.intersection(key2)) 
  
    if (commonKeys == 0): 
        print(count1 + count2) 
    else: 
        print((max(count1, count2)-commonKeys))
s1='bcadeh'
s2='heafg'
removechar(s1,s2)
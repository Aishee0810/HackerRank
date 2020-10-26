#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:47:34 2019

@author: aishee
"""

def score(n):
    table=[0 for i in range(n+1)]
    table[0]=1
    for j in range(1,n+1):
        table[j]+=table[j-1]
    for j in range(2,n+1):
        table[j]+=table[j-2]
    for j in range(3,n+1):
        table[j]+=table[j-3]
    print(table[n])
s=13
score(s)
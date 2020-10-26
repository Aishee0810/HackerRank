#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:25:26 2019

@author: aishee
"""

import os
def maximumtoys(prices,k):
    prices.sort()
    count=0
    sum=0
    while(sum!=k):
        for i in range(len(prices)):
            sum+=prices[i]
    print(sum)
    print(i+1)
prices=[1,12,5,111,200 ,1000 ,10]
print(prices)
k=50
maximumtoys(prices,k)
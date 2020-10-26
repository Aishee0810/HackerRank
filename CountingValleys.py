# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valcnt=0
    level=0
    i=0
#    while(i<n):
#        if(s[i]=='D'):
#            if(i+1<n and s[i+1]=='D'):
#                valcnt+=1
#            while(i+1<n and s[i+1]!='U'):
#                i+=1
#        i+=1
#    for i in range(n):
#        if(s[i]=='U'):
#            level+=1
#            if(level==0):
#                valcnt+=1
#        else:
#            level-=1
#    return valcnt
    level=valley=0
    for i in range(n):
        if(s[i]=='U'):
            level+=1
            if(level==0):
                valley+=1
        else:
            level-=1
    
    return valley
input="DDDUUUDDDDDDUDUDUDUDD"
size=len(input)
result=countingValleys(size,input)
print(result)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:14:32 2019

@author: aishee
"""

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
#    index=j=0
#    bribe=temp=0
#    for index in range(len(q)):
#        if(q[index]>(index+3)):
#            print("Too chaotic")
#            break
#        else:
#            for j in range(len(q)-index-1):
#                if(q[j]>q[j+1] and q[j]-(j+3)<0):
#                #if((index-1)<0 and q[index-1]==index+1):
#                    temp=q[j]
#                    q[j]=q[j+1]
#                    q[j+1]=temp
#                    bribe+=1
#                    print(temp)
#                    print(q)
#                #print(bribe)
##                elif((index-2)>0 and q[index-2]==index+1):
##                    temp=q[index-2]
##                    q[index-2]=q[index-1]
##                    q[index-1]=q[index]
##                    q[index]=temp
##                    bribe+=2
#    #print(temp)
#    print(q)
#    print (bribe)
    index=j=0
    bribe=temp=f=0
    for index in range(len(q)):
        if(q[index]>(index+3)):
            f=1
            break
        else:
            for j in range(len(q)-index-1):
                if(q[j]>q[j+1] and q[j]-(j+3)<=0):
                    temp=q[j]
                    q[j]=q[j+1]
                    q[j+1]=temp
                    bribe+=1
    print(f)
    if(f==1):
        print("Too chaotic")
    else:
        print(q)
        print(bribe)
q=[]
t=2
i=0
q.append(2)
q.append(5)
q.append(1)
q.append(3)
q.append(4)
for i in range(t):
    minimumBribes(q)

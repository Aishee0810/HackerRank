#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:54:56 2019

@author: aishee
"""
import string
import numpy
def repeatedString(s, n):
#    count=0
#    for i in range(len(s)):
#       if(s[i]=='a'):
#          count+=1
#    print(count)
#    if(count!=0):
#        count*=int(n/len(s))
#        print(count)
#        if(n%len(s)!=0):
##            for i in range(n%len(s),n):
##                ss=s[:n%len(s)]
##                for i in range(len(ss)):
##                    if(ss[i]=='a'):
##                        count+=1
#            count+=n%len(s)
#    print(count)
     count=0
     for i in range(len(s)):
       if(s[i]=='a'):
          count+=1
     if(count!=0 and int(n/len(s))!=0):
        count*=int(n/len(s))
        #print(count)
        if(n%len(s)!=0):
              for i in range(n%len(s),n):
                  ss=s[:n%len(s)]
              for i in range(len(ss)):
                    if(ss[i]=='a'):
                        count+=1
            #count+=n%len(s)
     print(count)
#s='gfcaaaecbg'
s='abba'
n=3
repeatedString(s,n)
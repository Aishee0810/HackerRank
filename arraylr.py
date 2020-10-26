#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:37:33 2019

@author: aishee
"""

import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    d=d%len(a)
    for i in range(1,d):
        temp=a[0]
        for j in range(len(a)):
            a[j]=a[j+1]
        a[len(a)-1]=temp
    return a

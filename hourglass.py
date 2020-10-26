#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:58:27 2019

@author: aishee
"""

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum=[]
    if(len(arr)<3 or len(arr[0])<3):
        return -1
        for i in range(len(arr)-2):
            for j in range(len(arr[0])-2):
                sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
    return (max(sum))

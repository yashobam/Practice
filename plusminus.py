#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p=0
    m=0
    z=0
    length=len(arr)
    for i in range(length):
        if arr[i]<0:
            m+=1
        elif arr[i]>0:
            p+=1
        else:
            z+=1
    print(round(p/length,6))
    print(round(m/length,6))
    print(round(z/length,6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    maxx=sum(arr[:0]+arr[0+1:])
    mini=sum(arr[:0]+arr[0+1:])
    for i in range(0,len(arr),1):
    	if maxx<sum(arr[:i]+arr[i+1:]):
    		maxx=sum(arr[:i]+arr[i+1:])
    	elif mini>sum(arr[:i]+arr[i+1:]):
    		mini=sum(arr[:i]+arr[i+1:])
    print(mini,maxx)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
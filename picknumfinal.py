import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(arr):
    Max=0
    for i in range(len(arr)):
        for k in findallnext(arr,i):
            Range=[arr[i],arr[k]]
            path=findinrange(arr[i:],Range)
            if path>Max:
                Max=path
    return(Max)

def findinrange(aarr,Range):
    path=0
    if Range[0]==Range[1]:
        Range=[Range[0]]
    for i in range(len(aarr)):
        for j in Range:
            if j==aarr[i]:
                path+=1
    return path

def findallnext(arr,k):
    ans=[]
    for i in range(k+1,len(arr)):
        if abs(arr[k]-arr[i])<=1:
            ans.append(i)
    if ans==[] and k+1<len(arr) and abs(arr[k]-arr[k+1])<=1:
        ans=[k+1]
    return ans



s="66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66"
arr=[int(i) for i in s.split()]
print(pickingNumbers(arr))
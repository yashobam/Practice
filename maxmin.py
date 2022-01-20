import math
import os
import random
import re
import sys
import time

def maxMin(k, arr):
	arr.sort()
	diff=10**9+1
	for i in range(k-1,len(arr)):
		a=arr[i]-arr[i-k+1]
		#print(a,arr[i],arr[i-k+1],i,i-k+1)
		if a<diff:
			diff=a

	
	return (diff)

s='''5
10
20
40
80
400
401'''
arr=[int(i) for i in s.split("\n")]
print(maxMin(2,arr))
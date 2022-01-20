import math
import os
import random
import re
import sys

def twoArrays(k, A, B):
	A.sort()
	B.sort(reverse=True)
	print(A,B)
	for i in range(len(A)):
		if A[i]+B[i]<k:
			return "NO"
	return "YES"

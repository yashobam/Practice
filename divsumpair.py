import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
	num=0
	for i in range(n):
		for j in range(i+1,n):
			if (ar[i]+ar[j])%k==0:
				num+=1
	return num
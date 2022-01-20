import math
import os
import random
import re
import sys

def getTotalX(a, b):
	fac1=[]
	fac2=[]
	fac=[]


	for i in range(len(b)):
		for j in range(1,b[i]+1):
			if b[i]%j==0:
				if j not in fac2:
					fac2.append(j)
	rem=[]
	for i in range(len(b)):
		for j in fac2:
			if b[i]%j!=0 and j not in rem:
				rem.append(j)
	
	for i in rem:
		index=fac2.index(i)
		fac2=fac2[:index]+fac2[index+1:]

	for i in fac2:
		for j in a:
			if  i%j==0 and i not in fac:
				fac.append(i)
	rem=[]
	for i in range(len(a)):
		for j in fac:
			if j%a[i]!=0 and j not in rem:
				rem.append(j)
	
	for i in rem:
		index=fac.index(i)
		fac=fac[:index]+fac[index+1:]
	print(fac2)
	print(fac)
	return len(fac)


print(getTotalX([1],[100]))
"""
[2],[20,30,12]
[2,6],[24,36]
[2,4],[16,32,96]
[1],[100]
"""
import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
	Max=0
	indices=[]
	dic={}
	for j in range(len(queries)):
		a=queries[j][0]-1
		b=queries[j][1]
		k=queries[j][2]
		for i in range(a,b):
			if i not in dic:
				dic[i]=k
			else:
				dic[i]+=k
			if dic[i]>Max:
				Max=dic[i]


	return Max
f=open("in.txt","r")
arr=[[int(j) for j in i.split()] for i in f.readlines()]

print(arrayManipulation(10000000,arr))
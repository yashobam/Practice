import math
import os
import random
import re
import sys

def ismagic(arr):
	n=len(arr)
	magicconst=sum(arr[0])
	dia1=0
	dia2=0
	for i in range(n):
		if magicconst!=sum(arr[i]):
			return False
		a=[arr[j][i] for j in range(n)]
		if magicconst!=sum(a):
			return False
		dia1+=arr[i][i]
		dia2+=arr[i][n-i-1]
	if dia1!=magicconst or dia2!=magicconst:
		return False
	return True

def formingMagicSquare(s):
	n=len(s)
	costs=[]
	arr=[]
	for i in range(n):
		for j in range(n):
			for s1 in range(-1,2,2):
				for s2 in range(-1,2,2):
					for d1 in range(1,5):
						r=i
						c=j
						magic=[[0]*n for k in range(n)]
						for l in range(1,n*n+1):
							r=0 if r>=n else n-1 if r<0 else r
							c=0 if c>=n else n-1 if c<0 else c
							if magic[r][c]!=0:
								r=r-s1
								c=c-s2
								r=0 if r>=n else n-1 if r<0 else r
								c=0 if c>=n else n-1 if c<0 else c
								c=c-1 if d1==3 else c+1 if d1==4 else c
								r=r-1 if d1==1 else r+1 if d1==2 else r
								r=0 if r>=n else n-1 if r<0 else r
								c=0 if c>=n else n-1 if c<0 else c
							magic[r][c]=l
							r=r+s1
							c=c+s2
						if ismagic(magic):
							arr.append(magic)

	mini=90000000
	index=0
	for k in range(len(arr)):
		score=0
		for i in range(n):
			for j in range(n):
				score+=abs(arr[k][i][j]-s[i][j])
		if score<mini:
			mini=score
			index=k
	return mini

s=[[5,3,4],[1,5,8],[6,4,2]]
t=[[4,8,2],[4,5,7],[6,1,6]]
u=[[4,5,8],[2,4,1],[1,9,7]]
print(formingMagicSquare(s))
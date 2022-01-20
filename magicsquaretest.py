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
		print (a)
		if magicconst!=sum(a):
			return False
		dia1+=arr[i][i]
		dia2+=arr[i][n-i-1]
	if dia1!=magicconst or dia2!=magicconst:
		return False
	return True

def makemagic1(n,r,c):
	magic=[[0]*n for i in range(n)]
	for i in range(1,n*n+1):
		r=0 if r>=n else n-1 if r<0 else r
		c=0 if c>=n else n-1 if c<0 else c
		if magic[r][c]==0:
			magic[r][c]=i
			r+=1
			c-=1
		else:
			r-=1
			c+=1
			r=0 if r>=n else n-1 if r<0 else r
			c=0 if c>=n else n-1 if c<0 else c
			c+=1
			c=0 if c>=n else n-1 if c<0 else c
			magic[r][c]=i
			r+=1
			c-=1
	return magic

def makemagic0(n,r,c,s1,s2,d1):
	magic=[[0]*n for i in range(n)]
	for i in range(1,n*n+1):
		r=0 if r>=n else n-1 if r<0 else r
		c=0 if c>=n else n-1 if c<0 else c
		if magic[r][c]==0:
			magic[r][c]=i
			r=r+s1
			c=c+s2
		else:
			r=r-s1
			c=c-s2
			r=0 if r>=n else n-1 if r<0 else r
			c=0 if c>=n else n-1 if c<0 else c
			c=c-1 if d1==3 else c+1 if d1==4 else c
			r=r-1 if d1==1 else r+1 if d1==2 else r
			r=0 if r>=n else n-1 if r<0 else r
			c=0 if c>=n else n-1 if c<0 else c
			magic[r][c]=i
			r=r+s1
			c=c+s2
	return magic

def checkeqall(n):
	arr=[]
	#file=open("AllArr.txt","w")
	#s=""
	c=1
	for i in range(n):
		for j in range(n):
			for s1 in range(-1,2,2):
				for s2 in range(-1,2,2):
					for d1 in range(1,5):
						mat=makemagic0(n,i,j,s1,s2,d1)
						#s+="r={} c={} s1={} s2={} d1={} at {}\n".format(i,j,s1,s2,d1,c)
						c=c+1
						#for k in range(n):
							#s+="{}\n".format(mat[k])
						arr.append(mat)
	#file.write(s)
	#file.close()
	s=""
	file=open("AllMat.txt","w")
	c=1
	for i in range(2*2*4*n*n):
		if ismagic(arr[i]):
			s+="{} matrix at {} is magic\n".format(c,i+1)
			c+=1
			for k in range(n):
				s+="{}\n".format(arr[i][k])
	file.write(s)
	file.close()
	s=""


def similarity(arr1,arr2):
	n=len(arr1)
	score=0
	for i in range(n):
		for j in range(n):
			score+=abs(arr1[i][j],arr1[i][j])
	return score

n=3
#checkeqall(n)

ismagic()
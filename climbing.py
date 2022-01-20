#started at 10:30pm 15/7/2021 finished 4am 16/7/2021

import math
import os
import random
import re
import sys
#first one is using recursion
def climbingLeaderboardrecur(rank,player):
	#Implement Binary search to find score
	rank=list(dict.fromkeys(rank))
	maxrank=len(rank)
	ranks=[]
	#print(rank)
	#print(player)
	for i in player:
		if i<=rank[0] and i>=rank[-1]:
			ranks.append(binsearch(rank,i,1))
		elif i>=rank[0]:
			ranks.append(1)
		elif i<rank[-1]:
			ranks.append(maxrank+1)
		elif i==rank[-1]:
			ranks.append(maxrank)

	return ranks

def binsearch(arr,sc,rank):

	mid=int((len(arr)-1)/2)

	if sc==arr[mid]:
		print(arr,mid,sc,rank)
		return rank+mid

	elif sc<arr[mid] and sc>arr[mid+1]:
		print(arr,mid,sc,rank)
		return rank+1+mid

	elif sc<arr[mid]:
		print(arr,mid,arr[mid+1:],sc,rank+(mid))
		return binsearch(arr[mid+1:],sc,rank+mid+1)

	elif sc>arr[mid]:
		print(arr,mid,arr[:-mid],sc,rank)
		return binsearch(arr[:-mid],sc,rank)
	
def climbingLeaderboard(rank,player):
	#Implement Binary search to find score

	rank=list(dict.fromkeys(rank))
	maxrank=len(rank)
	ranks=[]
	for i in player:
		lower=0
		upper=maxrank-1
		mid=int((upper)/2)+1
		if i<rank[0] and i>rank[-1]:
			while(True):
				if i==rank[mid]:
					ranks.append(mid+1)
					break
				elif upper==mid and upper-lower==1:
					ranks.append(mid+1)
					break
				elif i>rank[mid]:
					upper=mid
					mid=lower+int((upper-lower)/2)
				elif i<rank[mid]:
					temp=mid
					mid=lower+int((upper-lower)/2)+1
					lower=temp
		elif i>=rank[0]:
			ranks.append(1)
		elif i<rank[-1]:
			ranks.append(maxrank+1)
		else:
			ranks.append(maxrank)

	return ranks


print(climbingLeaderboard(arr1,arr2))
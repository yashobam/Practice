import math
import os
import random
import re
import sys

def getMinimumCost(k, c):
	c.sort(reverse=True)
	n=len(c)
	co=0
	people=[0]*k
	pcost=[0]*k
	cost=0
	for i in range(n):
		co=co if co<k else 0
		if k<i:
			people[co]+=1
			cost=cost+people[co]*c[i]
			pcost[co]+=people[co]*c[i]
			co+=1
		else:
			people[co]+=1
			cost=cost+people[co]*c[i]
			pcost[co]+=people[co]*c[i]
			co+=1
	return(cost,pcost)



print(getMinimumCost(1,[1,2,3,4]))



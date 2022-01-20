import math
import os
import random
import re
import sys

def migratoryBirds(arr):
	birds={}
	for i in range(len(arr)):
		if arr[i] in birds:
			birds[arr[i]]+=1
		else:
			birds[arr[i]]=1
	Maxk=list(birds.keys())[0]
	Max=birds[Maxk]
	for i in birds:
		if birds[i]>Max:
			Max=birds[i]
			Maxk=i
		elif birds[i]==Max and Maxk>i:
			Max=birds[i]
			Maxk=i
	return Maxk

print(migratoryBirds([1,4,4,4,5,3]))
#[1,1,2,2,3]
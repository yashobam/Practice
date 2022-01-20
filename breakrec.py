import math
import os
import random
import re
import sys

def breakingRecords(scores):
	minbreak=0
	maxbreak=0
	curmin=scores[0]
	curmax=scores[0]
	for i in scores:
		if curmin>i:
			curmin=i
			minbreak+=1
		elif curmax<i:
			curmax=i
			maxbreak+=1
	return [maxbreak,minbreak]

print(breakingRecords([10,5,20,20,4,5,2,25,1]))

"""
[12,24,10,24]
[10,5,20,20,4,5,2,25,1]
"""
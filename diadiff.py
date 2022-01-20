import math
import os
import random
import re
import sys

def diagonalDifference(arr):
	# Write your code here
	dia1=0
	dia2=0
	length=len(arr)
	for i in range(length):
		dia1+=arr[i][i]
		dia2+=arr[i][length-i-1]
		print(arr[i][i],arr[i][length-i-1])
	return abs(dia1-dia2)

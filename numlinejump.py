import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
	if x1>x2 and v1>=v2:
		return "NO"
	elif x1<x2 and v1<=v2:
		return "NO"
	elif ((x1-x2)/(v2-v1))-int((x1-x2)/(v2-v1))!=0.0:
		return "NO"
	else:
		return "YES"

print(kangaroo(0,3,4,2))
print(kangaroo(0,2,5,3))
print(kangaroo(21,6,47,3))
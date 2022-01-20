import math
import os
import random
import re
import sys
import time

def ashtonString(s, k):
	#arr=list(s)
	#arr.sort()
	#s="".join(arr)
	paths=[]
	for i in range(len(s)):
		for j in range(i,len(s)):
			if s[i:j+1] not in paths:
				paths.append(s[i:j+1])

	paths.sort()
	print(("".join(paths)),("".join(paths))[k-1])
	return ("".join(paths))[k-1]

ashtonString("abcdefghijk",1)
import math
import os
import random
import re
import sys

def matchingStrings(strings, queries):
	s={}
	ans=[]
	for val in strings:
		if val not in s:
			s[val]=1
		else:
			s[val]+=1
	for i in queries:
		if i in s:
			ans.append(s[i])
		else:
			ans.append(0)
	return ans

print(matchingStrings(["ab","ab","abc"],["ab","abc","bc"]))

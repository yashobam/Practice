import math
import os
import random
import re
import sys

def jimOrders(orders):
	a={}
	x=[]
	for key,val in enumerate(orders):
		a[key]=sum(val)
	a=sorted(a.items(), key=lambda item: item[1])
	for i in a:
		x.append(i[0]+1)
	return x
print(jimOrders([[1,3],[2,3],[3,3]]))
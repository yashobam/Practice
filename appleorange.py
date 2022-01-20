import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
	distapplemin=s-a
	distapplemax=t-a
	distorangemin=t-b
	distorangemax=s-b
	numapp=0
	numorg=0
	for i in apples:
		if i>=distapplemin and i<=distapplemax:
			numapp+=1
	for i in oranges:
		if i<=distorangemin and i>=distorangemax:
			numorg+=1
	print(numapp)
	print(numorg)
countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])
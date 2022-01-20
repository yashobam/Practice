import math
import os
import random
import re
import sys

def maximumToys(prices, k):
	prices.sort()
	Max=0
	while (k-prices[Max]>=0):
		k=k-prices[Max]
		Max=Max+1
	return(Max)

print(maximumToys([1,12,5,111,200,1000,10],50))


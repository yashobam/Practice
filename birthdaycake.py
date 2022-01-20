
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
	c=0
	maxx=max(candles)
	for i in candles: 
		if i==maxx:
			c=c+1
	return c

print(birthdayCakeCandles([4,4,1,3]))
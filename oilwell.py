import math
import os
import random
import re
import sys

def oilWell(blocks):
    # Write your code here
    r=len(blocks)
    c=len(blocks[0])
    wells=[]
    for i in range(r):
        for j in range(c):
            if blocks[i][j]==1:
                wells.append([i,j])



#oilWell([[1,0,0,0],[1,0,0,0],[0,0,1,0]])
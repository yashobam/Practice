import math
import os
import random
import re
import sys
import time

def dnahealth():
    scores=[]
    n = int(input().strip())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    genhel={}
    
    for i in range(len(genes)):
        if genes[i] not in genhel:
            genhel[genes[i]]=[i]
        else:
            genhel[genes[i]]=sorted(genhel[genes[i]]+[i])
    
    Min=10**9+1
    Max=0
    s = int(input().strip())
    st=time.time()
    for i in range(s):
        inp = input().rstrip().split()
        start = int(inp[0])
        end = int(inp[1])
        d = inp[2]
        score=0
        for i in range(len(d)):
            for j in range(i,len(d)):
                if d[i:j+1] in genhel:
                    for k in genhel[d[i:j+1]]:
                        if k>=start and k<=end:
                            score+=health[k]
                        elif k>end:
                            break

        scores.append(score)
    print(min(scores),max(scores))
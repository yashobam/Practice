import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    t=s.split(":")
    H=int(t[0])
    M=int(t[1])
    S=int(t[2][:2])
    AMPM=t[2][2:]
    if H==12 and AMPM=="AM":
        H-=12
    elif H!=12 and AMPM=="PM":
        H+=12

    return "{:02d}:{:02d}:{:02d}".format(H,M,S) 

print(timeConversion("07:05:45AM"))
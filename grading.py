import math
import os
import random
import re
import sys


def gradingStudents(grades):
    for i in range(len(grades)):
        nextmult=5*math.ceil(grades[i]/5)
        dist=nextmult-grades[i]
        print(nextmult,dist)
        grades[i]=grades[i] if grades[i]<38 else nextmult if dist<3 else grades[i]
    return grades

print(gradingStudents([73,67,38,33]))
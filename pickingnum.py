import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
'''
def pickingNumbers(a):
    # Write your code here
    length=len(a)
    elems=[a[i] for i in range(length-1) if a[i]!=a[i+1]]
    elems=elems+[a[-1]]
    i=0
    Max=[]
    while(i<length):
        if i<length-1 and abs(a[i]-a[i+1])<=1:
            temp,index=1,2
            i=index
            if len(temp)>=len(Max):
                Max=temp
                print (Max)
        i=i+1
    print(Max)
'''
def findnext(arr,k):
    curr=arr[k]
    for i in range(k+1,len(arr)):
        if abs(curr-arr[i])<=1:
            return i
            break
    return -1
    

def findall(arr,k):
    curr=arr[k]
    ans=[]
    for i in range(k+1,len(arr)):
        if abs(curr-arr[i])<=1:
            ans.append(i)
    return ans
'''
def pickingNumbers(arr):
    graph={}
    for i in range(len(arr)):
        graph[i]=findall(arr,i)
    def dist(A,path,allpath,maxx):
        path=path+[arr[A]]

        if graph[A]==[]:
            if len(maxx)<len(path) and path not in allpath:
                allpath.append(path)
                maxx=path
        else:
            for i in graph[A]:
                dist(i,path,allpath,max(allpath) if allpath!=[] else path)

        return allpath

    maxx=[]
    for i in range(len(arr)):
        d=dist(i,[],[],maxx)
        for j in range(len(d)):
            for k in d:
                if len(maxx)<len(k):
                    maxx=k
    print(len(maxx),maxx)
'''

def pickingNumbers(arr):
    Max=0
    for i in range(len(arr)):
        for k in findallnext(arr,i):
            Range=[arr[i],arr[k]]
            path=findinrange(arr[i:],Range)
            if path>Max:
                Max=path
    return(Max)

def findinrange(aarr,Range):
    path=0
    if Range[0]==Range[1]:
        Range=[Range[0]]
    for i in range(len(aarr)):
        for j in Range:
            if j==aarr[i]:
                path+=1
    return path

def findallnext(arr,k):
    ans=[]
    for i in range(k+1,len(arr)):
        if abs(arr[k]-arr[i])<=1:
            ans.append(i)
    if ans==[] and k+1<len(arr) and abs(arr[k]-arr[k+1])<=1:
        ans=[k+1]
    return ans

'''
def find_paths(arr, start, end, path, allpaths):
    graph={}
    for i in range(len(arr)):
        graph[i]=findall(arr,i)

    if end in graph[start]:
        allpaths.append([start])
    else:
        newpath = path + [start]
        for edge in graph[start]:
            d = graph[start][edge]
            if dmax - d >= 0:  
                find_paths(arr, edge, newpath, allpaths, dmax - d)
            else:
                allpaths.append(newpath + [edge])
    return allpaths
'''


s="14 18 17 10 9 20 4 13 19 19 8 15 15 17 6 5 15 12 18 2 18 7 20 8 2 8 11 2 16 2 12 9 3 6 9 9 13 7 4 6 19 7 2 4 3 4 14 3 4 9 17 9 4 20 10 16 12 1 16 4 15 15 9 13 6 3 8 4 7 14 16 18 20 11 20 14 20 12 15 4 5 10 10 20 11 18 5 20 13 4 18 1 14 3 20 19 14 2 5 13"
arr=[int(i) for i in s.split()]
pickingNumbers(arr)


'''
Test cases
[4,6,5,3,3,1]
[1,1,2,2,4,4,5,5,5]
[1,2,2,3,1,2]
[1,1,2,2,4,4,5,5,5,8,6,6,6]
[1,2,3,4,5,5,8,6,6,6,6]
s="66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66"
s="4 2 3 4 4 9 98 98 3 3 3 4 2 98 1 98 98 1 1 4 98 2 98 3 9 9 3 1 4 1 98 9 9 2 9 4 2 2 9 98 4 98 1 3 4 9 1 98 98 4 2 3 98 98 1 99 9 98 98 3 98 98 4 98 2 98 4 2 1 1 9 2 4"
s="14 18 17 10 9 20 4 13 19 19 8 15 15 17 6 5 15 12 18 2 18 7 20 8 2 8 11 2 16 2 12 9 3 6 9 9 13 7 4 6 19 7 2 4 3 4 14 3 4 9 17 9 4 20 10 16 12 1 16 4 15 15 9 13 6 3 8 4 7 14 16 18 20 11 20 14 20 12 15 4 5 10 10 20 11 18 5 20 13 4 18 1 14 3 20 19 14 2 5 13"
arr=[int(i) for i in s.split()]
'''
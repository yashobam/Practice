def pickingNumbers(arr):
    paths=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j] and abs(arr[j]-arr[i])<=1:
                for k in findallnext(arr,j):
                    Range=[arr[i],arr[k]]
                    path=findinrange(arr[i:],Range)
                    #print(i,j,path,Range,arr[i:])
                    if path not in paths:
                        #print(path)
                        paths.append(path)
            elif abs(arr[j]-arr[i])<=1:
                Range=[arr[i],arr[j]]
                path=findinrange(arr[i:],Range)
                #print(i,j,path,Range,arr[i:])
                if path not in paths:
                    #print(path)
                    paths.append(path)


    Max=max(paths,key=lambda x:len(x))
    print(len(Max),Max)

def findinrange(aarr,Range):
    path=[]
    if Range[0]==Range[1]:
        Range=[Range[0]]
    for i in range(len(aarr)):
        for j in Range:
            if j==aarr[i]:
                path.append(aarr[i])
    return path

def findallnext(arr,k):
    ans=[]
    for i in range(k+1,len(arr)):
        if abs(arr[k]-arr[i])<=1:
            ans.append(i)
    if ans==[] and k+1<len(arr) and abs(arr[k]-arr[k+1])<=1:
        ans=[k+1]
    return ans



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
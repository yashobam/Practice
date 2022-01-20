

'''
def recur(arr,req,req1,path,paths):
	if req==0:
		paths.append(path)
	else:
		for i in range(len(arr)):
			if req-arr[i]>=0:
				print(arr,path,req,i)
				recur(arr,req-arr[i],req1,path+[arr[i]],paths)
				print(arr,path,req,i)
			
				

	return paths
arr=[2,2,1,3,2]

print(recur(arr,4,4,[],[]))
'''

#for all lengths of m and summing to d
def birthday(s, d, m):
	num=0
	length=m
	arr=s
	req=d
	paths=[]
	def recur(l,i,path):

		if i==len(arr) and l==length and sum(path)==req:
			if path not in paths:
				paths.append(path)
			return

		elif i==len(arr):
			return

		elif l==length and sum(path)==req:
			if path not in paths:
				paths.append(path)

		newpath=path+[arr[i]]
		if len(path)<=length and sum(path)<=req:
			recur(l,i+1,path)
		if len(newpath)<=length and sum(newpath)<=req:
			recur(l+1,i+1,newpath)

	recur(0,0,[])

	for i in paths:
		num+=1
		print(i)
	return(num)


#for all touching sections of length d and summing to d
def birthday(s, d, m):
	num=0
	for i in range(len(s)-m+1):
		print(s[i:i+m])
		if sum(s[i:i+m])==d:
			num+=1
	return num
	
'''
def recur(arr,k,length,path,paths):
	path=path+[arr[k]]
	for i in range(k+1,len(arr)):
		newpath=path
		if len(newpath)==length and newpath not in paths:
			paths.append(newpath)

		recur(arr,i,length,path,paths)
	return paths

for i in range(len([2,2,1,3,2])):
	print(recur([2,2,1,3,2],i,2,[],[]))

print(recur([2,2,1,3,2],4,2,[],[]))


print(birthday([5,2,2,1,5,3,2],9,3))
print(birthday([2,2,1,3,2],4,2))
print(birthday([1,2,1,3,2],3,2))
print(birthday([1,1,1,1,1,1],3,2))
'''

s="2 5 1 3 4 4 3 5 1 1 2 1 4 1 3 3 4 2 1"
arr=[int(i) for i in s.split()]
print(birthday(arr,18,7))
print(birthday([5,2,2,1,5,3,2],9,3))
print(birthday([2,2,1,3,2],4,2))
print(birthday([1,2,1,3,2],3,2))
print(birthday([4],4,1))
print(birthday([1,1,1,1,1,1],3,2))


'''def recur(Depth,k,x=0):
	if Depth==0 or k==0:
		print("Return")
		#print("1",k)
		return 1
	else: 
		for i in range(k+1):
			#print("before loop",i,Depth,x)
			if recur(Depth-1,i,x)==1 and Depth:
				x+=1
			#print("after loop",i,Depth,x)
		#print(Depth,x,k)
	
	return x'''


def func(num,depth):
	global s
	print(num)
	if depth==0:
		s+=1
	else:
		for i in range(num):
			s+=1
			#func(i,depth)
			func(i,depth-1)
		print("end",num)
		


global s
s=0
k=3
n=6
func(k,n-k)




def func(k,n):

	d=n-k
	if d==0:
		print(1)
		return

	arr=[[i+2 for i in range(k-1)]]
	for i in range(d-1):
		line=[i+3]
		for j in range(1,k-1):
			line+=[arr[-1][j]+line[-1]]
		arr.append(line)
	print(arr[-1][-1])



func(7,30)





'''T=int(input())
while(T!=0):
	a=input().split()
	n=int(a[0])
	k=int(a[1])
	func(k,n)
	T-=1'''
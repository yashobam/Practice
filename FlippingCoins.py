global ht
ht={0:set(),1:set()}

def func(HT,index1,index2):
	global ht
	#ht[0].update(list(range(index1,index2+1)))
	#ht[1].update(range(index1,index2+1))
	if HT==0:
		for i in range(index1,index2+1):
			try:
				ht[0].remove(i)
				#print(ht[0],ht[1],i)
				ht[1].add(i)
			except:
				try:
					ht[1].remove(i)
					ht[0].add(i)
				except:
					ht[0].add(i)

	else:
		x=0
		for i in range(index1,index2+1):

			if i in ht[1]:
				x=x+1
		print(x)

func(1,0,3)
func(0,1,2)
func(1,0,1)
func(1,0,0)
func(0,0,3)
func(1,0,3)
func(1,3,3)
print(ht)



'''
S=input().split()
N=int(S[0])
Q=int(S[1])
for i in range(Q):
	S=input().split()
	HT=S[0]
	index1=S[1]
	index2=S[2]
'''


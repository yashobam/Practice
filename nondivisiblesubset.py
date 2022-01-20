def nondiv(ar,k):
	mod=[i%k for i in ar]
	print(mod)
	vals={}
	for i in range(len(mod)):
		if mod[i] not in vals:
			vals[mod[i]]=1
		else:
			vals[mod[i]]+=1
	for i in range(k):
		


	
		



nondiv([19,10,12,10,24,25,22],4)
def func(st,q):
	o=st
	st=list(st)
	g={}
	for i in st:
		if i in g:
			g[i]+=1
		else:
			g[i]=1
	

	
	if len(st)/2<maxx:
		print("Case #{}: ".format(q)+"IMPOSSIBLE")
	else:
		v=set()
		for i in g:
			for k in range(g[i]):
				for j in range(len(st)):
					if i!=o[j] and j not in v:
						st[j]=i
						v.add(j)
						break
		
		print("Case #{}: ".format(q)+"".join(st))


func("starting",1)
#for i in range(int(input())):
#	func(input(),i+1)
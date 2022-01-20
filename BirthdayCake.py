def func(r1,r2,c1,c2,R,C,k,okay):
	c1=c1-1
	r1=r1-1
	l=c2-c1
	b=r2-r1
	n=0
	pointsx=(int(l/k)+int(l%k>0))
	pointsy=(int(b/k)+int(b%k>0))
	n=min(pointsx*(b-1) + (b)*(l-1), pointsy*(l-1) + (b-1)*(l))
	l1=0
	l2=0
	l3=0
	l4=0
	if c1!=0:
		l1+=int((c1+l)/k)+int((c1+l)%k>0)
		l2+=pointsy
		l3+=pointsy
		l4+=pointsy
	if c2!=C:
		l1+=pointsy
		l2+=pointsy
		l3+=int((C-c1)/k)+int((C-c2)%k>0)
		l4+=pointsy
	if r1!=0:
		l1+=pointsx
		l2+=int((r1+b)/k)+int((r1+b)%k>0)
		l3+=pointsx
		l4+=pointsx
	if r2!=R:
		l1+=pointsx
		l2+=pointsx
		l3+=pointsx
		l4+=int((R-r1)/k)+int((R-r2)%k>0)
	x=min(l1,l2,l3,l4)
	n+=x
	print("Case #{}: ".format(okay+1),n)

for i in range(int(input())):
	a=input().split()
	R=int(a[0])
	C=int(a[1])
	K=int(a[2])
	a=input().split()
	r1=int(a[0])
	c1=int(a[1])
	r2=int(a[2])
	c2=int(a[3])
	func(r1,r2,c1,c2,R,C,K,i)


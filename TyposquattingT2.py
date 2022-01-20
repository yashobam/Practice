mixups={"1":["i","l","!","|"],"i":["1","l","!","|"],"l":["i","1","!","|"],"!":["i","l","1","|"],"|":["i","l","!","1"],"s":["5","$"],"5":["s","$"],"$":["5","s"],"o":["0"],"0":["o"],"a":["@"],"@":["a"],"e":["3"],"3":["e"]}

originals={}
full=set()
for i in range(int(input())):
	inp=input().split(".")
	full.add(inp[0]+"."+inp[1])
	if inp[0] not in originals:
		originals[inp[0]]=set()
		originals[inp[0]].add(inp[1])
	else:
		originals[inp[0]].add(inp[1])

for i in range(int(input())):
	inp=input().split(".")
	name=inp[0]
	host=inp[1]
	if name in originals and host  in originals[name]:
		pass
	elif name in originals and host not in originals[name]:
		print(name+"."+host)
	else:
		name=name+"."+host
		for j in full:
			a=False
			if len(j)!=len(name):
				continue
			for k in range(len(j)):
				if j[k]!=name[k]:
					if j[k] in mixups:
						if name[k] not in mixups[j[k]]:
							
							break
					else:
						break
				else:
					if k==len(j)-1:
						a=True
			if a:
				print(name)




		 					





"""
2
palantir.com
apple.com
4
pal@ntir.biz
apple.org
apple.com
appleorchard.net
"""
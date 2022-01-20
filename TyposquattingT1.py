originals={}
for i in range(int(input())):
	inp=input().split(".")
	if inp[0] not in originals:
		originals[inp[0]]=set()
		originals[inp[0]].add(inp[1])
	else:
		originals[inp[0]].add(inp[1])
for i in range(int(input())):
	inp=input().split(".")
	#fakes.append(inp)
	name=inp[0]
	host=inp[1]
	if name in originals:
		if host not in originals[name]:
			print(name+"."+host)

"""
2
palantir.com
apple.com
4
palantir.biz
apple.org
apple.com
appleorchard.net
"""
import math
import os
import random
import re
import sys
import time
'''
def dnahealth():
	scores=[]
	f=open("input02.txt")
	n = int(f.readline().strip())
	genes = f.readline().rstrip().split()
	health = list(map(int, f.readline().rstrip().split()))
	genhel={}
	
	for i in range(len(genes)):
		if genes[i] not in genhel:
			genhel[genes[i]]=[i]
		else:
			genhel[genes[i]]=sorted(genhel[genes[i]]+[i])
	
	Min=10**9+1
	Max=0
	s = int(f.readline().strip())
	st=time.time()
	for i in range(s):
		inp = f.readline().rstrip().split()
		start = int(inp[0])
		end = int(inp[1])
		d = inp[2]
		score=0

		for i in range(len(d)):
			for j in range(i,len(d)):
				if d[i:j+1] in genhel:
					st=binsearch(genhel[d[i:j+1]],start)
					en=binsearch(genhel[d[i:j+1]],end)
					if en!=-2 or st!=-1:
						for k in genhel[d[i:j+1]][st:en+1]:
							score+=health[k]
					

		scores.append(score)
	print(min(scores),max(scores))

def binsearch(arr,num):
	
	lower=0
	upper=len(arr)-1
	point=(upper-1)//2
	if num>=arr[0] and num<arr[-1]:
		while lower<=upper:
			point=lower+(upper-1)//2
			if arr[point]==num:
				return point
			elif arr[point]<num and arr[point+1]>num:
				return point+1
			elif num<arr[point]:
				upper=point-1
			elif num>arr[point]:
				lower=point+1
	elif num ==arr[-1]:
		return len(arr)-1
	elif num>arr[-1]:
		return -1
	elif num<arr[0]:
		return -2
'''
'''
def dnahealth():
	scores=[]
	f=open("input02.txt")
	n = int(f.readline().strip())
	genes = f.readline().rstrip().split()
	health = list(map(int, f.readline().rstrip().split()))
	genhel={}
	
	for i in range(len(genes)):
		if genes[i] not in genhel:
			genhel[genes[i]]=[i]
		else:
			genhel[genes[i]]=sorted(genhel[genes[i]]+[i])
	
	s = int(f.readline().strip())
	st=time.time()
	for i in range(s):
		inp = f.readline().rstrip().split()
		start = int(inp[0])
		end = int(inp[1])
		d = inp[2]
		score=0

		for i in range(len(d)):
			for j in range(i,len(d)):
				if d[i:j+1] in genhel:
					if start>=genhel[d[i:j+1]][0] and end<=genhel[d[i:j+1]][-1]:
						for k in genhel[d[i:j+1]]:
							if k>=start and k<=end:
								score+=health[k]
							elif k>end:
								break

		scores.append(score)
	print(min(scores),max(scores))
'''

'''
def findPath(root,pointer=root,path=[],ans=[]):
	path=path+[pointer]
	if pointer.next==set():


	
	




	
	Paths=PathTillVal(root,node,[],[])
	x=0
	if Paths!=[]:
		Paths.sort(reverse=True,key=len)
		for path in Paths:
			if node not in path:
				#print(path)
				ans=path
				return path
	else:
		x=1

	if x!=1 and ans==[]:
		for path in Paths:
			if node not in path:
				findPath(root,path[-2],[])'''
'''
def traverse(root,word):
	pointer=root
	path=[]
	for i in range(len(word)):
		c=0
		for j in pointer.next:
			if word[i]==j.dna:
				c=1
				path.append(j)
				print(word[i],j.dna)
				pointer=j
				break
		if c==0:
			pointer=pointer.failure
			while()
				
			#traverse(pointer.failure,word[i:])
'''
'''def traverseWrecur(root,word,path=[],ans=[]):
	path=path+[root]
	if word=="":
		ans.append(path)
	else:
		c=0
		for i in root.next:
			if i.dna==word[0]:
				c=c+1
				traverse(i,word[1:],path,ans)
	return ans'''


class Node:
	def __init__(self,dna="",indices=set()):
		self.dna=dna
		self.indices=indices
		self.next=set()
		self.failure=None

def Print(root):
	print(root.dna)
	for node in root.next:
		Print(node)

def AddIn():
	root=Node()
	f=open("input01.txt")
	n = int(f.readline().strip())
	genes = f.readline().rstrip().split()
	health = list(map(int, f.readline().rstrip().split()))
	c=0
	
	for i in range(len(genes)):
		pointer=root
		for ele in list(genes[i]):
			k=0
			for j in pointer.next:
				if ele==j.dna:
					k=j
					break
			if k==0:
				node=Node(ele)
				pointer.next.add(node)
				pointer=node
			else:
				pointer=k
		if c==0:
			x=node
		c=c+1
		pointer.failure=root
		pointer.indices.add(i)
	return root,x

def PrintAllWords(root,tillnow):
	tillnow=tillnow+root.dna
	if root.indices!=set():
		print(tillnow,root.indices,root.failure)
		#print(tillnow)
	for i in root.next:
		PrintAllWords(i,tillnow)

def traverse(root,word):
	pointer=root
	path=[]
	c=0
	while(word!=""):
		c=0
		for j in pointer.next:
			if word[0]==j.dna:
				c=1
				path.append(j)
				pointer=j
				break
		if c==0:
			pointer=pointer.failure
		else:
			word=word[1:]
	return(path)


def PathTillVal(root,val,Nodes=[],past=[]):
	past=past+[root]
	#print(len(Nodes),len(past))
	#len(past)>2 and 
	if past[-1].dna==val:
		#print(Nodes,past)
		Nodes.append(past)
		#print(root.dna,past)
	for i in root.next:
		PathTillVal(i,val,Nodes,past)
	#print(Nodes,past)
	return Nodes


def pathTillNode(root,node,Nodes=[],past=[]):
	past=past+[root]
	if root==node:
		Nodes.append(past)
	for i in root.next:
		pathTillNode(i,node,Nodes,past)
	return Nodes


'''
def failureLinks(root,pointer):
	for i in pointer.next:
		Paths=pathTillNode(root,i)
		print(Paths)
		if Paths!=[]:
			Paths=Paths[0]
			valpath=PathTillVal(root,i.dna)
			x=[]
			for j in valpath:
				temp=""
				for k in j:
					temp+=k.dna
				x.append(temp)

			for l in range(len(Paths)):
				temp=["".join(k.dna) for k in Paths[l:]]
				temp="".join(temp)
				for j in range(len(x)):
					if x[j]==temp:
						i.failure=valpath[j][0]
						print(temp,i.failure)
'''






root,node=AddIn()
#PrintAllWords(root,"")
print(failureLinks(root,root))

'''for i in pathTillNode(root,node):
	for j in i:
		print(j.dna,end="")
	print()'''




'''t=traverse(root,"abcdeabcd")
if t!=[]:
	for i in t:
		print(i.dna,end="")
else:
	print("No places")'''

'''Maxpath=findPath(root,node)
print(Maxpath,node.dna)
for i in Maxpath:
	print(i.dna,end=" ")'''

#failurelinks(root,[])
'''
pathstill=PathTillVal(root,node,[],[])
print(pathstill,node.dna)
for i in pathstill:
	for j in i:
		print(j.dna,end='')
	print()
'''



#print(node.dna)

#failurelink(root,node,[])
'''
for i in max(PathTillVal(root,a,[],[]), key=len):
	print(i.dna)'''
#print(searchAdd(AddIn(),"",{}))
#PrintAllWords(AddIn(),"")
#searchAdd(AddIn(),"")
import math
import os
import random
import re
import sys
import time
'''
def minimumLoss(price):
	loss=10**16
	for i in range(len(price)):
		for j in range(i+1,len(price)):
			#print(price[j]-price[i],price[i],price[j])
			if price[j]<price[i] and price[i]-price[j]<loss:
				y1=i
				y2=j
				loss=price[i]-price[j]
	return loss
'''
'''
def minimumLoss(price):
	loss=10**16+1
	a={val:key for key,val in enumerate(price)}
	#a=dict(sorted(a.items(),reverse=True))
	for i in range(len(price)):
		
		
	return loss
'''

'''def minimumLoss(price):
	loss=10**16
	
	for i in range(len(price)):
		for j in range(i+1,len(price)):
			if price[j]<price[i] and price[i]-price[j]<loss:
				loss=price[i]-price[j]
	return loss'''

class Node:
	def __init__(self,num=None):
		self.left=None
		self.right=None
		self.num=num
		self.indices=set()


class Tree:
	def __init__(self,num):
		self.root=Node(num)
		self.root.indices.add(0)


	def addNode(self,num,index):
		pointer=self.root

		while True:
			if pointer.num<num:
				if pointer.right!=None:
					pointer=pointer.right
				else:
					pointer.right=Node(num)
					pointer.right.indices.add(index)
					return pointer.right

			elif pointer.num>num:
				if pointer.left!=None:
					pointer=pointer.left
				else:
					pointer.left=Node(num)
					pointer.left.indices.add(index)
					return pointer.left
			else:
				pointer.indices.add(index)
				return pointer

	'''def addAfter(self,root,num):
		pointer=root
		if pointer.num<num:
			pointer.right=Node(num)
			return pointer.right
		else:
			pointer.left=Node(num)
			return pointer.left'''

	def printTree(self,node, level=0):
		if node != None:
			self.printTree(node.right, level + 1)
			print(' ' * 4 * level + '->', node.num,node.indices)
			self.printTree(node.left, level + 1)

	def search(self,root,num):
		if root==None or root.num==num:
			return root
		if root.num<num:
			return self.search(root.right,num)
		else:
			return self.search(root.left,num)



def minimumLoss(price):
	tree=Tree(price[0])
	nodes=[tree.root]
	#print(price[1:])
	for i in range(1,len(price)):
		nodes.append(tree.addNode(price[i],i))
	tree.printTree(tree.root)
	a=[]
	root=tree.root
	#nodes.sort(reverse=True,key=lambda a:a.num)
	#print(nodes)
	#print(nodes[0].num)
	for i in range(len(nodes)):
		pointer=nodes[i]
		#print(nodes[i].num)
		path=Path(root,nodes[i])
		#print(path)
		
		path=path[0]
		path.reverse()
		#for m in path:
		#	print(m,m.num)
		for j in path:
			if j.num>pointer.num:
				#print("greater",pointer.num,j.num,i)
				break
			left=LeftSubtree(j.left)
			#for m in left:
				#print(m.num)
			for k in left:
				#print(pointer.num,k.num,i,max(k.indices))
				if i<max(k.indices):
					#print(pointer.num,k.num,i,max(k.indices))
					a.append(pointer.num-k.num)
					break

	#print(a)
	print(min(a))






def LeftSubtree(root,ans=[]):
	if root:
		#print(root.num)
		#ans.append(root)
		LeftSubtree(root.right,ans)
		print(root.num)
		#ans.append(root)
		LeftSubtree(root.left,ans)
		#print(root.num)
		#ans.append(root)
	return ans


	


def Path(root,node,path=[],paths=[]):
	path=path+[root]
	if root==None or root.num==node.num:
		paths.append(path)
	elif root.num<node.num:
		Path(root.right,node,path,paths)
	else:
		Path(root.left,node,path,paths)
	return paths
	

'''
p1=node.left
		if p1!=None:
			while p1.right!=None and p1.right:
				p1=p1.right
		if p1!=None and max(p1.indices):
			print(p1.num,node.num)
			#a.append(i.num-p1.num)'''






'''
def findClosest(root,node):
	if root.left is None and root.right is None:
		if root.num==node.num:
			return root
		else:
			return None
	elif root.right is None:
		if root.left.num>=node.num:
			return findClosest(root.left,node)
		else:
			return None
	elif root.left is None:
		if root.right.num>=node.num:
			return findClosest(root.right,node)
		else:
			return None
	elif node.num>root.left.num and node.num<root.right.num:
		Min=10**16+1
		if node.num>0:

	elif node.num>root.left.num:
		return findClosest(root.right,node)
	elif node.num<root.right.num:
		return findClosest(root.right,node)

'''
'''for i in range(len(nodes)):
		p1=nodes[i].left
		if p1!=None:
			while p1.right!=None and p1.right:
				p1=p1.right
		if p1!=None:
			print(p1.num,i.num)
			a.append(i.num-p1.num)

		else:
			print(p1,i.num)'''


f=open("min1.txt","r")
n=int(f.readline())
arr=list(map(int, f.readline().split()))

minimumLoss(arr)


'''
f=open("in.txt","r")
s=time.time()
arr=[int(i) for i in f.readline().split()]
print(time.time()-s)
'''
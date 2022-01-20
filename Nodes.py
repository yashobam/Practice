class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None


#printing out list from Node
def Print(root):
	pointer=root
	while pointer:
		print(pointer.data)
		pointer=pointer.next
'''
#Making some nodes
n1=Node("a")
n2=Node("b")
n3=Node("c")
n4=Node("e")
#assigning nexts in nodes
n1.next=n2
n2.next=n3
n3.next=n4

#printing Linked list
Print(n1)

'''
'''
#insert an element in middle of list where it is in lexicological order
def SoretedInsert(root,ele):
	eleNode=Node(ele)
	pointer=root
	while pointer:
		if pointer.data<ele:
			prev=pointer
			pointer=pointer.next
		else:
			prev.next=eleNode
			eleNode.next=pointer
			break

SoretedInsert(n1,"d")
Print(n1)
'''

#Class for Node with Multiple nexts
class NodeWMulti:
	def __init__(self,data=None):
		self.data=data
		self.next={}
#Making some nodes
n1=NodeWMulti("a")
n2=NodeWMulti("b")
n3=NodeWMulti("c")
n4=NodeWMulti("e")
#assigning nexts in nodes
n1.next.append(n2)
n2.next.append(n3)
n2.next.append(n4)
n1.next.append(n3)

def PrintMulti(root):
	print(root.data)
	for node in root.next:
		PrintMulti(node)

PrintMulti(n2)

#add in a particular way
def Add(root,ele):
	root.next.add(NodeWMulti(ele))
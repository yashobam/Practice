class Node:
	def __init__(self,num=None):
		self.left=None
		self.right=None
		self.num=num
		

class Tree:
	def __init__(self,num):
		self.root=Node(num)


	def addNode(self,num):
		pointer=self.root

		while True:
			if pointer.num<num:
				if pointer.right!=None:
					pointer=pointer.right
				else:
					pointer.right=Node(num)
					return

			elif pointer.num>=num:
				if pointer.left!=None:
					pointer=pointer.left
				else:
					pointer.left=Node(num)
					return


	def printTree(self,node, level=0):
		if node != None:
			self.printTree(node.right, level + 1)
			print(' ' * 4 * level + '->', node.num)
			self.printTree(node.left, level + 1)

	def search(self,root,num):
		if root==None or root.num==num:
			return root
		if root.num<num:
			return self.search(root.right,num)
		return self.search(root.left,num)






BinaryTree=Tree(13)
BinaryTree.addNode(15)
BinaryTree.addNode(8)
BinaryTree.addNode(10)
BinaryTree.addNode(11)
BinaryTree.printTree(BinaryTree.root)
node=BinaryTree.search(BinaryTree.root,15)
if node is not None:
	print(node,node.num)
else:
	print("Not in list")
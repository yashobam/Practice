import copy


class pall:
	def __init__(self,board,rows,cols):
		self.board=copy.deepcopy(board)
		self.rows=rows
		self.cols=cols
		self.prev=[]
		self.empty=set()
		for i in range(rows):
			for j in range(cols):
				if self.board[i][j]==".":
					self.empty.add((i,j))

	def checkEmpty(self):
		a=copy.deepcopy(self.empty)
		for i,j in a:

			down=i
			while (down<self.rows and self.board[down][j]!="#"):
				down+=1
			down-=1

			up=i
			while (up>=0 and self.board[up][j]!="#"):
				up-=1
			up+=1
			
			for k in range(up,down+1):
				if self.board[k][j]!=self.board[down-k+up][j]:
					if self.board[k][j].isalpha():
						self.board[down-k+up][j]=self.board[k][j]
						self.empty.remove((down-k+up,j))
					elif self.board[down-k+up][j].isalpha():
						self.board[k][j]=self.board[down-k+up][j]
						self.empty.remove((k,j))

			right=j
			while (right<self.cols and self.board[i][right]!="#"):
				right+=1
			right-=1

			left=j
			while (left>=0 and self.board[i][left]!="#"):
				left-=1
			left+=1

			
			for k in range(left,right+1):
				if self.board[i][k]!=self.board[i][right-k+left]:
					if self.board[i][k].isalpha():
						self.board[i][right-k+left]=self.board[i][k]
						self.empty.remove((i,right-k+left))
					elif self.board[i][right-k+left].isalpha():
						self.board[i][k]=self.board[i][right-k+left]
						self.empty.remove((i,k))

	def print(self):
		for i in range(self.rows):
			for j in range(self.cols):
				print(self.board[i][j],end="")
			print()
	def run(self):
		for i in range(len(self.empty)):
			self.checkEmpty()
			if self.prev==self.board:
				break
			self.prev=copy.deepcopy(self.board)
	def returnboard(self):
		return self.board
'''

s="""A...#.
B##...
B.###.
A...#."""
s="""##################################################
	##.#.....#.....#.....#.....#.....#################
	##.#.###.#.###.#.###.#.###.#.###.#################
	##...#...#...#...#...#...#...#...#################
	######.#####.#####.#####.#####.###################
	##...#...#...#...#.#...#.#...#...#################
	##.#.###.#.###.#.#.#.#.#.#.#.###.#################
	##.#.....#.....#.#...#...#.#.....#################
	##.#############.#########.#######################
	##...#.......#...#...#...#.#.....#################
	####.#.#####.#.###.#.#.#.#.#.###.#################
	##...#...#...#...#.#...#.#...#...#################
	##.#####.#.#####.#.#####.#####.###################
	##.#...#.#.#...#.#...#...#...#...#################
	##.#.#.#.#.#.#.#.###.#.###.#.###.#################
	##...#...#...#...#...#.....#.....#################
	##################.###############################
	##...#...#...#...#...#.....#.....#################
	##.#.#.#.#.#.#.#.###.#.###.#.###.#################
	##.#...#.#.#...#.#...#...#...#...#################
	##.#####.#.#####.#.#####.#####.###################
	##...#...#...#...#.#...#.#...#...#################
	####.#.#####.#.###.#.#.#.#.#.###.#################
	##...#.......#...#...#...#.#.....#################
	##.#############.#########.#######################
	##.#.....#.....#.#...#...#.#.....#################
	##.#.###.#.###.#.#.#.#.#.#.#.###.#################
	##...#...#...#...#.#...#.#...#...#################
	######.#####.#####.#####.#####.###################
	##...#...#...#...#...#...#...#...#################
	##.#.###.#.###.#.###.#.###.#.###.#################
	##.#....R#.....#.....#.....#.....#################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################
	##################################################"""
board=[]
for i in s.split():
	temp=[]
	for j in i:
		temp.append(j)
	board.append(temp)
rows=len(board)
cols=len(board[0])
Test=pall(board,rows,cols)
Test.run()
Test.print()
'''
	
f=open("ts2_input.txt","r")
w=open("out.txt","w")

for k in range(int(f.readline())):
	board=[]
	a=f.readline().split(" ")
	N=int(a[0])
	for i in range(N):
		temp=[]
		s=f.readline()
		#print(s)
		for j in s[:-1]:
			temp.append(j)
		board.append(temp)
	rows=len(board)
	cols=len(board[0])

	Test=pall(board,rows,cols)
	Test.run()
	ans=Test.returnboard()

	c=0
	for i in range(rows):
		for j in range(cols):
			if ans[i][j]!=board[i][j]:
				c+=1
	print(c)
	w.write("Case #{}: {}\n".format(k+1,c))
	for i in range(rows):
		for j in range(cols):
			w.write(ans[i][j])
		w.write("\n")
f.close()
w.close()
f=open("ts1_output.txt","r")
w=open("out.txt","r")

#complete([1])


# s="""A..A#.
# B##A..
# BB###.
# A..A#."""
# s="""A..A#.
# B##A..
# BB###.
# A..A#."""

'''python PallindromicCrossword.py
100
1 1
T
1 50
..AB##B...K.O..PQ..AJ......O.YR.EMU..UO..XS...REL.'''
"""
for k in range(int(input())):
	board=[]
	a=input().split(" ")
	N=int(a[0])
	for i in range(N):
		temp=[]
		s=input()
		for j in s:
			temp.append(j)
		board.append(temp)

	
	rows=len(board)
	cols=len(board[0])

	Test=pall(board,rows,cols)
	Test.run()
	ans=Test.returnboard()

	c=0
	for i in range(rows):
		for j in range(cols):
			if ans[i][j]!=board[i][j]:
				c+=1
	print("Case #{}:".format(k+1),c)
	for i in range(rows):
		for j in range(cols):
			print(ans[i][j],end="")
		print()
"""


'''2
2 2
A.
.#
4 6
A...#.
B##...
B.###.
A...#.
'''
struct node:
	n,x,y=(-1,-1,-1)

class head:
	def __init__(self):
		self.x=10
		self.y=12
		node n
		node.n=10
		node.x=11
		node.y=12
	# def add(self):
	# 	self.y=1222
	def Print(self):
		self.add()
		print(self.x,self.y)

class sub1(head):
	def __init__(self):
		head.__init__(self)
		self.z=18
		self.Print()
	def add(self):
		self.y=130

class sub2(head):
	def __init__(self):
		head.__init__(self)
		self.z=10
		self.Print()
	def add(self):
		self.y=100

# h=head()
s1=sub1()
s2=sub2()
# h.Print()
# s1.Print()
# s2.Print()
# s1.add()
# s2.add()
# s1.Print()
# s2.Print()


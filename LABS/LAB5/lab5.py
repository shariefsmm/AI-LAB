import numpy as np
import Queue
# a=np.zeros((3,3),dtype='int')
# a[1][2]=35
 # print(a)
# 2 1 3 5 4 6 7 8 9

class environment:
	def __init__(self):
		# self.n=int(input("Enter n:"))
		self.n=4
		l=[1,2,3,4,5,6,7,8,9,10,'b',11,13,14,15,12]
		self.pos=Queue.Queue(100)
		self.start_state=np.array(l).reshape(self.n,self.n)
		self.pos.put((2,2))
		# self.start_state=np.zeros((self.n,self.n),dtype='int')
		# print("Enter elements:")
		# for i in range(0,self.n):
		# 	for j in range(0,self.n):
		# 		self.a[i][j]=int(input(""))
		# l=[i for i in range(1,self.n*self.n)]
		# print(l)
		# while 1:
		# 	l=[i for i in range(1,self.n*self.n)]
		# 	# l.append('b')
		# 	np.random.shuffle(l)
		# 	p=np.random.randint(0,self.n)
		# 	print(l)
		# 	l.insert(p,'b')
		# 	x=p/self.n
		# 	y=p%self.n
		# 	self.pos.put((x,y))
		# 	print(l)
		# 	self.start_state=np.array(l).reshape(self.n,self.n)
		# 	if self.parity(self.start_state,x,y)==0:break
		self.q=Queue.Queue(100)
		self.q.put(self.start_state)

	def is_goal(self,a):
		b=a.flatten()
		for i in range(0,self.n*self.n-1):
			# print(int(b[i]),i+1)
			print(type(b[i]))
			if np.int(b[i])!=i+1:return False
		return True



	def parity(self,a,x,y):
		count=0
		b=a.flatten()
		for i in range(0,self.n*self.n):
			if b[i]=='b':continue
			for j in range(i+1,self.n*self.n):
				if b[j]=='b':continue
				if b[j]<b[i]:count+=1
		self.d=(self.n-1-x)+(self.n-1-y)
		par=(count+self.d)%2
		return par

class agent:
	def Action(self,a,x,y):
		# print("Enter",x,y)
		action="R"
		if action=="R":
			b=a.copy()
			if y+1<s.n:
				(b[x][y],b[x][y+1])=(b[x][y+1],b[x][y])
				# (s.a[s.x][s.y],s.a[s.x][s.y+1])=(s.a[s.x][s.y+1],s.a[s.x][s.y])
				s.q.put(b)
				s.pos.put((x,y+1))
				# s.y+=1;
				# s.parity()
		# print("LOST")
		action="L"
		if action=="L":
			b=a.copy()
			# print(b,x,y)
			if y-1>=0:
				# print(b[x][y],b[x][y-1])
				(b[x][y],b[x][y-1])=(b[x][y-1],b[x][y])
				# print(b)
				s.q.put(b)
				s.pos.put((x,y-1))
				# (s.a[s.x][s.y],s.a[s.x][s.y-1])=(s.a[s.x][s.y-1],s.a[s.x][s.y])
				# s.y-=1;
				# s.parity()
		# print("U")
		action="U"
		if action=="U":
			b=a.copy()
			if x-1>=0:
				(b[x][y],b[x-1][y])=(b[x-1][y],b[x][y])
				s.q.put(b)
				s.pos.put((x-1,y))
				# (s.a[s.x][s.y],s.a[s.x-1][s.y])=(s.a[s.x-1][s.y],s.a[s.x][s.y])
				# s.x-=1;
				# s.parity()
		# print("D")
		action="D"
		if action=="D":
			b=a.copy()
			if x+1<s.n:
				# print("TEST")
				(b[x][y],b[x+1][y])=(b[x+1][y],b[x][y])
				# print("TEST",s.q.qsize())
				s.q.put(b)
				# print("TEST")
				s.pos.put((x+1,y))
				# (s.a[s.x][s.y],s.a[s.x+1][s.y])=(s.a[s.x+1][s.y],s.a[s.x][s.y])
				# s.x+=1;
				# s.parity()
		print("LOST")

	def BFS(self):
		while s.q.empty()==False:
			a=s.q.get()
			print("HELLO",s.q.qsize())
			print(a)
			(x,y)=s.pos.get()
			if s.is_goal(a):
				print("Goal state reached")
				return
			self.Action(a,x,y)
			# print("hi")
		print("Not reachable")

s=environment()
A=agent()
A.BFS()
# s.parity()
# print(s.a)

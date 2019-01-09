# python2
import numpy as np
import Queue
# a=np.zeros((3,3),dtype='int')
# a[1][2]=35
 # print(a)
# 2 1 3 5 4 6 7 8 9

class environment:
	def __init__(self):
		self.n=4

		l=[1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12]
		self.start_state=np.array(l).reshape(self.n,self.n)
		self.x=1
		self.y=2


		# while 1:
		# 	l=[i for i in range(1,self.n*self.n)]
		# 	np.random.shuffle(l)
		# 	p=np.random.randint(0,self.n)
		# 	# print(l)
		# 	l.insert(p,self.n*self.n)
		# 	self.x=p/self.n
		# 	self.y=p%self.n
		# 	# self.pos.put((x,y))
		# 	# print(l)
		# 	self.start_state=np.array(l).reshape(self.n,self.n)
		# 	if self.parity(self.start_state,self.x,self.y)==0:break

		print(self.start_state)
		# self.q.put(self.start_state)

	def is_goal(self,a):
		b=a.flatten()
		for i in range(0,self.n*self.n):
			if b[i]!=i+1:return False
		return True



	def parity(self,a,x,y):
		count=0
		b=a.flatten()
		for i in range(0,self.n*self.n):
			# if b[i]=='-1':continue
			for j in range(i+1,self.n*self.n):
				# if b[j]=='-1':continue
				if b[j]<b[i]:count+=1
		self.d=(self.n-1-x)+(self.n-1-y)
		par=(count+self.d)%2
		return par

class model:
	def __init__(self,a,pos,parent):
		self.a=a
		self.pos=pos
		self.parent=parent

class agent:
	def __init__(self):
		# self.pos=Queue.Queue(1000)
		# self.q=Queue.Queue(1000)
		# self.p=Queue.Queue(1000)
		# self.q.put(s.start_state)
		# self.pos.put((s.x,s.y))
		t=model(s.start_state,(s.x,s.y),-1)
		self.l=[]
		self.l.append(t)
		self.count=0
		self.q=Queue.Queue(10000)
		self.q.put(0)
		self.v=[]
		self.BFS()

	def cmp(self,a,b):
		A=a.flatten()
		B=b.flatten()
		for i in range(0,s.n*s.n):
			if A[i]!=B[i]:return 0
		return 1

	def check(self,b):
		for i in range(len(self.v)):
			if self.cmp(self.v[i],b)==1:return 1
		return 0

	def Action(self,current,a,x,y):
		# print("Enter",x,y)
		action="R"
		if action=="R":
			b=a.copy()
			if y+1<s.n:
				(b[x][y],b[x][y+1])=(b[x][y+1],b[x][y])
				# if self.check(b)==0:
				t=model(b,(x,y+1),current)
				self.l.append(t)
				self.count+=1
				self.q.put(self.count)
				# self.q.put(b)
				# self.pos.put((x,y+1))
				# self.p.put(a)
				
		action="L"
		if action=="L":
			b=a.copy()
			if y-1>=0:
				(b[x][y],b[x][y-1])=(b[x][y-1],b[x][y])
				# if self.check(b)==0:
				t=model(b,(x,y-1),current)
				self.l.append(t)
				self.count+=1
				self.q.put(self.count)
				# self.q.put(b)
				# self.pos.put((x,y-1))
				# self.p.put(a)
		
		action="U"
		if action=="U":
			b=a.copy()
			if x-1>=0:
				(b[x][y],b[x-1][y])=(b[x-1][y],b[x][y])
				# if self.check(b)==0:
				t=model(b,(x-1,y),current)
				self.l.append(t)
				self.count+=1
				self.q.put(self.count)
				# self.q.put(b)
				# self.pos.put((x-1,y))
				# self.p.put(a)
		
		action="D"
		if action=="D":
			b=a.copy()
			if x+1<s.n:
				(b[x][y],b[x+1][y])=(b[x+1][y],b[x][y])
				# if self.check(b)==0:
				t=model(b,(x+1,y),current)
				self.l.append(t)
				self.count+=1
				self.q.put(self.count)
				# self.q.put(b)
				# self.pos.put((x+1,y))
				# self.p.put(a)

	def Print(self,index):
		t=[]
		print("Path is as follows:")
		while(index!=-1):
			t.append(index)
			index=self.l[index].parent
		for i in range(len(t)-1,-1,-1):
			print(self.l[t[i]].a)

	def BFS(self):
		while self.q.empty()==False:
			current=self.q.get()
			if self.check(self.l[current].a):
				# print("hello",self.l[current].a)
				continue
			# print(self.l[current].a)
			self.v.append(self.l[current].a)
			# (x,y)=self.pos.get()
			(x,y)=self.l[current].pos
			if s.is_goal(self.l[current].a):
				self.Print(current)
				return
			self.Action(current,self.l[current].a,x,y)
			
		print("Not reachable")

s=environment()
A=agent()
# A.BFS()

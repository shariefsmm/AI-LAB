import numpy as np
import heapq
from random import randint
import math

class environment:
	def __init__(self):
		self.n=5
		self.grid=np.zeros(self.n*self.n,dtype='int').reshape(self.n,self.n);
		self.start=(0,0)
		self.goal=(self.n-1,self.n-1)
		self.generate_grid()
		print self.grid

	def generate_grid(self):
		l=self.n/2
		for i in range(0,l):
			x,y=randint(0,self.n-1),randint(0,self.n-1)
			p,q=randint(0,self.n-1),randint(0,self.n-1)
			if x>p: (x,p)=(p,x)
			if y>q: (y,q)=(q,y)
			if (x==0 and y==0) or (p==self.n-1 and q==self.n-1):continue
			for j in range(x,p+1):
				for k in range(y,q+1):
					self.grid[j][k]=1;
		x,y=randint(0,self.n-1),randint(0,self.n-1)
		for i in range(0,x+1):
				self.grid[i][0]=0
		for i in range(0,y+1):
				self.grid[x][i]=0
		for i in range(x,self.n):
				self.grid[i][y]=0
		for i in range(y,self.n):
				self.grid[self.n-1][i]=0

class Manhattan:
	def __init__(self):
		self.v=np.zeros(s.n*s.n,dtype='int').reshape(s.n,s.n);
		self.p=[ [(-1,-1) for i in range(0,s.n)] for j in range(0,s.n) ]
		self.h=[]
		self.BFS()

	def Distance(self,x,y):
		return abs(x-(s.n-1) )+abs(y-(s.n-1))
	def action(self,x,y,g):
		if x<s.n-1 and self.v[x+1][y]==0 and s.grid[x+1][y]==0:	# right
			self.p[x+1][y]=(x,y)
			distance=self.Distance(x+1,y)
			heapq.heappush(self.h,(g+1+distance,(x+1,y,g+1)))
			# print(self.h)
		if x>0 and self.v[x-1][y]==0 and s.grid[x-1][y]==0:		# left
			self.p[x-1][y]=(x,y)
			distance=self.Distance(x-1,y)
			heapq.heappush(self.h,(g+1+distance,(x-1,y,g+1)))
		if y<s.n-1 and self.v[x][y+1]==0 and s.grid[x][y+1]==0:	# down
			self.p[x][y+1]=(x,y)
			distance=self.Distance(x,y+1)
			heapq.heappush(self.h,(g+1+distance,(x,y+1,g+1)))
		if y>0 and self.v[x][y-1]==0 and s.grid[x][y-1]==0:	# up
			self.p[x][y-1]=(x,y)
			distance=self.Distance(x,y-1)
			heapq.heappush(self.h,(g+1+distance,(x,y-1,g+1)))

	def Print(self):
		l=[]
		l.append((s.n-1,s.n-1))
		(x,y)=self.p[s.n-1][s.n-1]
		print("Manhattan heuristic path: ")
		while 1:
			if x==0 and y==0:
				l.append((0,0))
				break
			l.append((x,y))
			(x,y)=self.p[x][y]
		for i in range(len(l)-1,-1,-1):
			print(l[i])
		print(" ")


	def BFS(self):
		heapq.heapify(self.h)
		heapq.heappush(self.h,(self.Distance(0,0),(0,0,0)))
		while self.h:
			(count,(x,y,g))=heapq.heappop(self.h)
			if x==s.n-1 and y==s.n-1:
				self.Print()
				break
			# print(x,y)
			self.v[x][y]=1
			self.action(x,y,g)
			# print(self.h)
		# print("exit")

class Euclidian:
	def __init__(self):
		self.v=np.zeros(s.n*s.n,dtype='int').reshape(s.n,s.n);
		self.p=[ [(-1,-1) for i in range(0,s.n)] for j in range(0,s.n) ]
		self.h=[]
		self.BFS()

	def Distance(self,x,y):
		return math.sqrt( (x-(s.n-1))**2 +(y-(s.n-1))**2)
	def action(self,x,y,g):
		if x<s.n-1 and self.v[x+1][y]==0 and s.grid[x+1][y]==0:	# right
			self.p[x+1][y]=(x,y)
			distance=self.Distance(x+1,y)
			heapq.heappush(self.h,(g+1+distance,(x+1,y,g+1)))
			# print(self.h)
		if x>0 and self.v[x-1][y]==0 and s.grid[x-1][y]==0:		# left
			self.p[x-1][y]=(x,y)
			distance=self.Distance(x-1,y)
			heapq.heappush(self.h,(g+1+distance,(x-1,y,g+1)))
		if y<s.n-1 and self.v[x][y+1]==0 and s.grid[x][y+1]==0:	# down
			self.p[x][y+1]=(x,y)
			distance=self.Distance(x,y+1)
			heapq.heappush(self.h,(g+1+distance,(x,y+1,g+1)))
		if y>0 and self.v[x][y-1]==0 and s.grid[x][y-1]==0:	# up
			self.p[x][y-1]=(x,y)
			distance=self.Distance(x,y-1)
			heapq.heappush(self.h,(g+1+distance,(x,y-1,g+1)))

	def Print(self):
		l=[]
		l.append((s.n-1,s.n-1))
		(x,y)=self.p[s.n-1][s.n-1]
		print("Euclidian heuristic path: ")
		while 1:
			if x==0 and y==0:
				l.append((0,0))
				break
			l.append((x,y))
			(x,y)=self.p[x][y]
		for i in range(len(l)-1,-1,-1):
			print(l[i])
		print(" ")


	def BFS(self):
		heapq.heapify(self.h)
		heapq.heappush(self.h,(self.Distance(0,0),(0,0,0)))
		while self.h:
			(count,(x,y,g))=heapq.heappop(self.h)
			if x==s.n-1 and y==s.n-1:
				self.Print()
				break
			# print(x,y)
			self.v[x][y]=1
			self.action(x,y,g)
			# print(self.h)
		# print("exit")

s=environment()
a=Manhattan();
b=Euclidian();

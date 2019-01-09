import numpy as np
import heapq
from random import randint
import math

class Environment:
	def __init__(self):
		self.n=17
		self.l=[]
		self.l.append((0,0))
		self.l.append((1,0))
		self.l.append((2,0))
		self.l.append((5,0))
		self.l.append((0,1))
		self.l.append((1,1))
		self.l.append((3,1))
		self.l.append((4,1))
		self.l.append((5,1))
		self.l.append((6,1))
		self.l.append((0,2))
		self.l.append((3,2))
		self.l.append((5,2))
		self.l.append((6,2))
		self.l.append((0,3))
		self.l.append((3,3))
		self.l.append((5,3))
		f=open("d.txt","r")
		t1=[]
		self.d=[]
		while 1:
			t2=f.readline()
			if t2=="":break
			t1=list(t2.split(","))
			t3=[]
			for i in range(len(t1)-1):
				x=float(t1[i])
				t3.append(x)
			self.d.append(t3)
		self.source=0
		self.goal=13
		self.Bus=50.0
		self.Cycle=25.0
		self.budget=60.0
		self.rate=3.0

class Agent:
	def __init__(self):
		self.v=np.zeros(s.n,dtype='int');
		self.p=[ -1 for i in range(0,s.n)]
		self.h=[]
		self.BFS()

	def Print(self,time):
		print("Total time taken is %s"%(time))
		t=[]
		x=s.goal
		while x!=-1:
			t.append(x)
			# print(x)
			x=self.p[x]
		for i in range(len(t)-1,-1,-1):
			print(t[i])

	def BFS(self):
		heapq.heapify(self.h)
		heapq.heappush(self.h,(0,(s.source,-1,s.budget)))
		while self.h:
			(time,(node,P,b))=heapq.heappop(self.h)
			if self.v[node]==1:continue
			if self.v[node]==0:self.v[node]=1
			self.p[node]=P
			if node==s.goal:
				self.Print(time)
				break
			for i in range(0,s.n):
				x=s.d[node][i]
				if x!=-1:
					t=x/s.Cycle
					heapq.heappush(self.h,(time+t,(i,node,b)))
					if x>3:
						t=x/s.Bus
						cost=t*s.rate
						if b-cost>=0:
							heapq.heappush(self.h,(time+t,(i,node,b-cost)))


s=Environment()
a=Agent()



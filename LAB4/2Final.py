import numpy as np
import heapq
from random import randint
import math

class environment:
	def __init__(self):
		self.n=100
		self.grid=np.ones(self.n*self.n,dtype='int').reshape(self.n,self.n);
		self.start=(randint(0,self.n-1),randint(0,self.n-1))
		self.goal=(randint(0,self.n-1),randint(0,self.n-1))
		while self.goal == self.start : self.goal=(randint(0,self.n-1),randint(0,self.n-1))
		self.generate_grid()
		print("Start state is (%d,%d)"%(self.start[0],self.start[1]))
		print("Goal state is (%d,%d)"%(self.goal[0],self.goal[1]))
		self.Print()
		# print(self.grid)

	def Print(self):
		for i in range(0,self.n):
			for j in range(0,self.n):
				print("%d"%(self.grid[i][j]),end=" ")
			print("")

	def generate_grid(self):
		# Random blocking in grid
		l=int(self.n/2)
		for i in range(0,l):
			x,y=randint(0,self.n-1),randint(0,self.n-1)
			p,q=randint(0,self.n-1),randint(0,self.n-1)
			if x>p: (x,p)=(p,x)
			if y>q: (y,q)=(q,y)
			# if self.start==(x,y) or self.start==(p,q):continue
			# if self.goal==(x,y) or self.goal==(p,q):continue
			for j in range(x,p+1):
				for k in range(y,q+1):
					self.grid[j][k]=0

		self.grid[self.start[0]][self.start[1]]=1
		self.grid[self.goal[0]][self.goal[1]]=1

		# creating a random path from start to goal state
		x,y=randint(0,self.n-1),randint(0,self.n-1)
		# print(x,y)

		tempMin,tempMax=(x,self.start[0])
		if x>self.start[0]:(tempMin,tempMax)=(tempMax,tempMin)
		for i in range(tempMin,tempMax+1):
					self.grid[i][self.start[1]]=1

		tempMin,tempMax=(y,self.start[1])
		if y>self.start[1]:(tempMin,tempMax)=(tempMax,tempMin)
		for i in range(tempMin,tempMax+1):
				self.grid[x][i]=1

		tempMin,tempMax=(x,self.goal[0])
		if x>self.goal[0]:(tempMin,tempMax)=(tempMax,tempMin)
		for i in range(tempMin,tempMax+1):
				self.grid[i][y]=1

		tempMin,tempMax=(y,self.goal[1])
		if y>self.goal[1]:(tempMin,tempMax)=(tempMax,tempMin)
		for i in range(tempMin,tempMax+1):
				self.grid[self.goal[0]][i]=1
		# self.grid[self.start[0]][self.start[1]]=3
		# self.grid[self.goal[0]][self.goal[1]]=4

s=environment()

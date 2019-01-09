import numpy as np
# a=np.zeros((3,3),dtype='int')
# a[1][2]=35
 # print(a)
# 2 1 3 5 4 6 7 8 9

class environment:
	def __init__(self):
		self.n=int(input("Enter n:"))
		self.a=np.zeros((self.n,self.n),dtype='int')
		print("Enter elements:")
		for i in range(0,self.n):
			for j in range(0,self.n):
				self.a[i][j]=int(input(""))
		self.x=self.n-1
		self.y=self.n-1

	def parity(self):
		count=0
		for i in range(0,self.n):
			for j in range(0,self.n):
				if (i,j)==(self.x,self.y):
					self.d=(self.n-1-i)+(self.n-1-j)
					continue
				for k in range(i,self.n):
					for l in range(0,self.n):
						if (k,l)==(self.x,self.y):continue
						if i==k and j<l:
							if(self.a[k][l]<self.a[i][j]):count+=1
						if i<k:
							if(self.a[k][l]<self.a[i][j]):count+=1
		par=(count+self.d)%2
		print(par)

class agent:
	def Action(self):
		if self.action=="R":
			if s.y+1<s.n:
				(s.a[s.x][s.y],s.a[s.x][s.y+1])=(s.a[s.x][s.y+1],s.a[s.x][s.y])
				s.y+=1;
				s.parity()
		if self.action=="L":
			if s.y-1>=0:
				(s.a[s.x][s.y],s.a[s.x][s.y-1])=(s.a[s.x][s.y-1],s.a[s.x][s.y])
				s.y-=1;
				s.parity()
		if self.action=="U":
			if s.x-1>=0:
				(s.a[s.x][s.y],s.a[s.x-1][s.y])=(s.a[s.x-1][s.y],s.a[s.x][s.y])
				s.x-=1;
				s.parity()
		if self.action=="D":
			if s.x+1<s.n:
				(s.a[s.x][s.y],s.a[s.x+1][s.y])=(s.a[s.x+1][s.y],s.a[s.x][s.y])
				s.x+=1;
				s.parity()
s=environment()
s.parity()
# print(s.a)

import numpy as np
# a=np.zeros((3,3),dtype='int')
# a[1][2]=35
 # print(a)
# 2 1 3 5 4 6 7 8 9

class environment:
	def __init__(self):
		self.n=4


		# self.n=int(input("Enter n:"))
		# self.a=np.zeros((self.n,self.n),dtype='int')
		# print("Enter elements:")
		# for i in range(0,self.n):
		# 	for j in range(0,self.n):
		# 		self.a[i][j]=int(input(""))
		# self.x=self.n-1
		# self.y=self.n-1

		#create list of n*n elements
		l=[i for i in range(1,self.n*self.n)]

		# shuffle the list
		np.random.shuffle(l)

		#randomly insert n*n element in the shuffled list
		p=np.random.randint(0,self.n)
		l.insert(p,self.n*self.n)
		self.x=p/self.n
		self.y=p%self.n

		#convert the above list to array
		self.start_state=np.array(l).reshape(self.n,self.n)

		# print the array and its parity
		print(self.start_state)
		print("Parity is %d"%(self.parity(self.start_state,self.x,self.y)))

	
	def parity(self,a,x,y):
		count=0
		b=a.flatten()
		for i in range(0,self.n*self.n):
			for j in range(i+1,self.n*self.n):
				if b[j]<b[i]:count+=1
		self.d=(self.n-1-x)+(self.n-1-y)
		par=(count+self.d)%2
		return par

class agent:
	def Action(self):
		if self.action=="R":
			if s.y+1<s.n:
				(s.a[s.x][s.y],s.a[s.x][s.y+1])=(s.a[s.x][s.y+1],s.a[s.x][s.y])
				s.y+=1;
				# s.parity()
		if self.action=="L":
			if s.y-1>=0:
				(s.a[s.x][s.y],s.a[s.x][s.y-1])=(s.a[s.x][s.y-1],s.a[s.x][s.y])
				s.y-=1;
				# s.parity()
		if self.action=="U":
			if s.x-1>=0:
				(s.a[s.x][s.y],s.a[s.x-1][s.y])=(s.a[s.x-1][s.y],s.a[s.x][s.y])
				s.x-=1;
				# s.parity()
		if self.action=="D":
			if s.x+1<s.n:
				(s.a[s.x][s.y],s.a[s.x+1][s.y])=(s.a[s.x+1][s.y],s.a[s.x][s.y])
				s.x+=1;
				# s.parity()
s=environment()
# s.parity()
# print(s.a)

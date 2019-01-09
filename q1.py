
import numpy as np
import Queue
import heapq
import math as mat

class environment:
	def __init__(self):

		#	Take input from user
		self.n=int(input("Enter n:"))
		self.start_state=np.zeros((self.n,self.n),dtype="int").reshape(self.n,self.n)
		print("Enter elements:")
		for i in range(0,self.n):
			for j in range(0,self.n):
				self.start_state[i][j]=int(input(""))
				if(self.start_state[i][j]==(self.n*self.n-1)):self.pos1=[i,j]
				if(self.start_state[i][j]==(self.n*self.n)):self.pos2=[i,j]
		print("Given input:")
		print(self.start_state)

	def is_goal(self,a):
		#	check if matrix a is the goal state or not
		b=a.flatten()
		for i in range(0,self.n*self.n-2):
			if np.int(b[i])!=i+1:return False
		return True

# For each node we create a model to store information of the node
class model:
	def __init__(self,a,pos1,pos2,parent,g,my,action):
		self.a=a  				# matrix(state)
		self.pos1=pos1			# blank1 position
		self.pos2=pos2			# blank2 position
		self.parent=parent		# parent node index
		self.g=g 				# cost so far
		self.my=my 				# it's index in list
		self.action=action 		# Action made on its parent node

class agent:
	def __init__(self):
		self.l={"12"} 	# set of visited matrices(in strings)
		self.count=0 	# count = no:of nodes so far
		self.v=[] 		# list to store the created nodes
		self.h=[]		# priority heapq list
		heapq.heapify(self.h)	
		self.BFS()

	# calculate manhattan distance of matrix a
	def distance(self,a):
		ans = 0
		for i in range(s.n):
			for j in range(s.n):
				k = a[i][j] - 1
				if k >= s.n ** 2 - 2:
					continue
				x = k // s.n
				y = k % s.n
				ans += abs(x - i) + abs(y - j)
		return ans

	# converts current matrix into string
	def STR(self,a,pos1,pos2):
		st = []
		for i in range(0,s.n):
			for j in range(0,s.n):
				st.append(chr(ord('a') + a[i][j] - 1))
		[u,v]=pos1
		st[u * s.n + v] = chr(ord('a') + s.n ** 2 - 2)
		[u,v]=pos2
		st[u * s.n + v] = chr(ord('a') + s.n ** 2 - 2)
		return ''.join(st)

	def Action(self,g,current,a,x,y,pos,m):
		action="U"
		if action=="U":
			b=a.copy()
			if (x-1)>=0 and [x-1,y]!=pos:
				(b[x][y],b[x-1][y])=(b[x-1][y],b[x][y])
				if(m==1):
					t=model(b,[x-1,y],pos,current,g+1,self.count,(1,"Up"))
					self.v.append(t)
					heapq.heappush(self.h,(g+1+self.distance(b),(self.count)))
					self.count+=1
				if(m==2):
					t=model(b,pos,[x-1,y],current,g+1,self.count,(2,"Up"))
					self.v.append(t)
					heapq.heappush(self.h,(g+1+self.distance(b),(self.count)))
					self.count+=1

		
		action="D"
		if action=="D":
			b=a.copy()
			if (x+1)<s.n and [x+1,y]!=pos:
				(b[x][y],b[x+1][y])=(b[x+1][y],b[x][y])
				if(m==1):
					t=model(b,[x+1,y],pos,current,g+1,self.count,(1,"Down"))
					self.v.append(t)
					heapq.heappush(self.h,(g+1+self.distance(b),(self.count)))
					self.count+=1
				if(m==2):
					t=model(b,pos,[x+1,y],current,g+1,self.count,(2,"Down"))
					self.v.append(t)
					heapq.heappush(self.h,(g+1+self.distance(b),(self.count)))
					self.count+=1

		action="L"
		if action=="L":
			b=a.copy()
			if (y-1)>=0 and [x,y-1]!=pos:
				(b[x][y],b[x][y-1])=(b[x][y-1],b[x][y])
				if(m==1):
					t=model(b,[x,y-1],pos,current,g+1,self.count,(1,"Left"))
					self.v.append(t)
					heapq.heappush(self.h,(g+1+self.distance(b),(self.count)))
					self.count+=1
				if(m==2):
					t=model(b,pos,[x,y-1],current,g+1,self.count,(2,"Left"))
					self.v.append(t)
					heapq.heappush(self.h,(g+1+self.distance(b),(self.count)))
					self.count+=1
		action="R"
		if action=="R":
			b=a.copy()
			if (y+1)<s.n and [x,y+1]!=pos:
				(b[x][y],b[x][y+1])=(b[x][y+1],b[x][y])
				if(m==1):
					t=model(b,[x,y+1],pos,current,g+1,self.count,(1,"Right"))
					self.v.append(t)
					heapq.heappush(self.h,(g+1+self.distance(b),(self.count)))
					self.count+=1
				if(m==2):
					t=model(b,pos,[x,y+1],current,g+1,self.count,(2,"Right"))
					self.v.append(t)
					heapq.heappush(self.h,(g+1+self.distance(b),(self.count)))
					self.count+=1
		
		
	# To print the path once goal state reached
	def Print(self,index,g):
		t=[]
		print("\nPath is as follows:")
		while(index!=-1):
			t.append(index)
			index=self.v[index].parent
		for i in range(len(t)-1,-1,-1):
			x,y=self.v[t[i]].action
			if x!=-1:
				if x==1:x=s.n*s.n-1
				else: x=s.n*s.n
				print("Move %d in %s"%(x,y))
			print(self.v[t[i]].a)
			print("\n")
		print("Total length is %d"%(g))

	def BFS(self):
		t=model(s.start_state,s.pos1,s.pos2,-1,0,0,(-1,"S"))
		self.v.append(t)
		self.count+=1
		heapq.heappush(self.h,(0+self.distance(s.start_state),(0)))
		while self.h:
			(A,(index))=heapq.heappop(self.h)
			t=self.v[index]
			S=self.STR(t.a,t.pos1,t.pos2)
			if S in self.l:continue
			self.l.add(S)
			x=self.v[index].my
			if s.is_goal(self.v[index].a):
				self.Print(index,self.v[index].g)
				return
			self.Action(self.v[index].g,x,self.v[index].a,self.v[index].pos1[0],self.v[index].pos1[1],self.v[index].pos2,1)
			self.Action(self.v[index].g,x,self.v[index].a,self.v[index].pos2[0],self.v[index].pos2[1],self.v[index].pos1,2)
			
		print("Not reachable")

s=environment()
MY_agent=agent()

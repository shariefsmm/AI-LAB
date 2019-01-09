

import numpy as np
import Queue
import heapq
import math as mat

class environment:
	def __init__(self):
		#	Take input from user
		self.n=int(input("Enter n:"))
		self.grid=np.zeros(self.n*self.n,dtype='int').reshape(self.n,self.n)
		# self.start=(randint(0,self.n-1),randint(0,self.n-1))
		# self.goal=(randint(0,self.n-1),randint(0,self.n-1))
		self.wc=[0,0]
		self.rc=[0,0]
		print("Enter white coordinate position: ")
		self.wc[0]=int(input(""))
		self.wc[1]=int(input(""))
		print("Enter red coordinate position: ")
		self.rc[0]=int(input(""))
		self.rc[1]=int(input(""))
		self.start=(0,0)
		self.grid[self.wc[0]][self.wc[1]]=1
		self.grid[self.rc[0]][self.rc[1]]=2
		# self.goal=(self.n-1,self.n-1)
		# self.generate_grid()
		print self.grid

	def is_goal(self,rc):
		if rc==[0,self.n-1]:return True
		else: return False

# For each node we create a model to store information of the node
class model:
	def __init__(self,a,wp,rp,parent,g,my,action):
		self.a=a  				# matrix(state)
		self.wp=wp			# blank1 position
		self.rp=rp			# blank2 position
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
	def Distance(self,wp,rp):
		ans=0
		ans=abs(wp[0]-rp[0])+abs(wp[1]-rp[1])
		ans+=abs(rp[0]-1)+abs(rp[1]-s.n-1)
		return ans

	# converts current matrix into string
	def STR(self,wp,rp):
		st = []
		st.append(chr(ord('a')+wp[0]))
		st.append(chr(ord('a')+wp[1]))
		st.append(chr(ord('a')+rp[0]))
		st.append(chr(ord('a')+rp[1]))
		# for i in range(0,s.n):
		# 	for j in range(0,s.n):
		# 		st.append(chr(ord('a') + a[i][j] - 1))
		# [u,v]=pos1
		# st[u * s.n + v] = chr(ord('a') + s.n ** 2 - 2)
		# [u,v]=pos2
		# st[u * s.n + v] = chr(ord('a') + s.n ** 2 - 2)
		return ''.join(st)

	def Action(self,a,g,wp,rp,p):
		temp=[0,0]
		[x,y]=wp
		temp[0]=rp[0]
		temp[1]=rp[1]
		b=a.copy()
		if x<s.n-1:	# down
			# self.p[x+1][y]=(x,y)
			(b[x][y],b[x+1][y])=(b[x+1][y],b[x][y])
			if temp==[x+1,y]:temp=[x,y]
			t=model(b,[x+1,y],temp,p,g+1,self.count,"down")
			self.v.append(t)
			distance=self.Distance((x+1,y),temp)
			heapq.heappush(self.h,(g+1+distance,(self.count)))
			self.count+=1
			

		temp=[0,0]
		[x,y]=wp
		temp[0]=rp[0]
		temp[1]=rp[1]
		b=a.copy()
		if x>0:	# up
			# self.p[x+1][y]=(x,y)
			(b[x][y],b[x-1][y])=(b[x-1][y],b[x][y])
			if temp==[x-1,y]:temp=[x,y]
			t=model(b,[x-1,y],temp,p,g+1,self.count,"up")
			self.v.append(t)
			distance=self.Distance((x-1,y),temp)
			heapq.heappush(self.h,(g+1+distance,(self.count)))
			self.count+=1



		temp=[0,0]
		[x,y]=wp
		temp[0]=rp[0]
		temp[1]=rp[1]
		b=a.copy()
		if y<s.n-1:	# right
			# self.p[x+1][y]=(x,y)
			(b[x][y],b[x][y+1])=(b[x][y+1],b[x][y])
			if temp==[x,y+1]:temp=[x,y]
			t=model(b,[x,y+1],temp,p,g+1,self.count,"right")
			self.v.append(t)
			distance=self.Distance((x,y+1),temp)
			heapq.heappush(self.h,(g+1+distance,(self.count)))
			self.count+=1


		temp=[0,0]
		[x,y]=wp
		temp[0]=rp[0]
		temp[1]=rp[1]
		b=a.copy()
		if y>0:	# left
			# self.p[x+1][y]=(x,y)
			(b[x][y],b[x][y-1])=(b[x][y-1],b[x][y])
			if temp==[x,y-1]:temp=[x,y]
			t=model(b,[x,y-1],temp,p,g+1,self.count,"left")
			self.v.append(t)
			distance=self.Distance((x,y-1),temp)
			heapq.heappush(self.h,(g+1+distance,(self.count)))
			self.count+=1


	def Print(self,index,g):
		t=[]
		print("\nPath is as follows:")
		while(index!=-1):
			t.append(index)
			index=self.v[index].parent
		for i in range(len(t)-1,-1,-1):
			x=self.v[t[i]].action
			if x!=-1:
				# temp=self.v[t[i]].wp
				# print("Move %d in %s"%(x,y))
				print(self.v[t[i]].a)
				print("Move "+x)
			# print(self.v[t[i]].a)
			print("\n")
		print("Total length is %d"%(g))
	def BFS(self):
		t=model(s.grid,s.wc,s.rc,-1,0,0,-1)
		self.v.append(t)
		self.count+=1
		heapq.heappush(self.h,(0+self.Distance(s.wc,s.rc),(0)))
		while self.h:
			(A,(index))=heapq.heappop(self.h)
			t=self.v[index]
			S=self.STR(t.wp,t.rp)
			# print(index,t.rp)
			if S in self.l:continue
			self.l.add(S)
			x=self.v[index].my
			if s.is_goal(t.rp):
				self.Print(index,self.v[index].g)
				return
			# self.Action(self.v[index].g,x,self.v[index].a,self.v[index].pos1[0],self.v[index].pos1[1],self.v[index].pos2,1)
			self.Action(t.a,self.v[index].g,t.wp,t.rp,index)

		print("Not reachable")


s=environment()
a=agent()

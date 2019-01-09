import numpy
import pickle
import math

r=pickle.load(open("road", "r"))
v=pickle.load(open("vehicle", "r"))
t=pickle.load(open("time", "r"))

# print(road)
# print(vehicle)
# print(time)

class environment:
	def __init__(self):
		self.size=r.shape
		self.road=[[0 for i in range(self.size[1])]for j in range(self.size[0])]
		self.time=0
	def update_time(self,e):
		p=[i.time for i in l]
		p.append(e)
		self.time=reduce(min,p)
		# if(e<self.time):self.time=e



class agent:
	def __init__(self,path,time):
		self.path=path
		self.count=1
		self.current_road=(path.item(0),path.item(1))
		self.time=self.update_time()
		self.size=path.shape
	def update(self):
		if(self.time==s.time):
			s.road[self.current_road[0]][self.current_road[1]]-=1
			self.count+=1
			if self.count<self.size[1]:
				y=self.path
				self.current_road=(y.item(self.count-1),y.item(self.count))
				# self.current_road[1]=self.path.item(self.count)
				s.road[self.current_road[0]][self.current_road[1]]+=1
				self.update_time()
	def update_time(self):
		x=s.road[self.current_road[0]][self.current_road[1]]-1
		self.speed=(math.exp(0.5*x)/(1+math.exp(0.5*x)))+15/(1+math.exp(0.5*x))
		self.time=s.time+r[self.current_road[0]].item(self.current_road[1])/self.speed


(m,n)=t.shape
s=environment()
# print(s.road)
l=[]
for i in range(m):
	# print("hi\n")
	current_time=t[i].item(0)
	s.update_time(current_time)
	if current_time<=s.time:
		vehicle=agent(v[i],current_time)
		l.append(vehicle)
		continue
	for j in l:
		j.update()
	i-=1

for i in l:
	print(i.time)

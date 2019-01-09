import numpy
import pickle
import math

# open files
r=pickle.load(open("road", "r"))
v=pickle.load(open("vehicle", "r"))
t=pickle.load(open("time", "r"))

class environment:
	def __init__(self):

		# get dimensions of road
		self.size=r.shape

		# road stores no:of vehicles present at each path
		self.road=[[0 for i in range(self.size[1])]for j in range(self.size[0])]

		""" min time among time of arri of next vehice and 
			exist vehicles curr path exit time"""
		self.time=0

	def update_time(self,e):	#e = next vehicle enter time
		p=[i.exit for i in l if i.active==1]
		p.append(e)

		# finds min time for next update
		self.time=reduce(min,p)


class agent:
	def __init__(self,path,time):
		self.path=path	
		self.enter=[time]	# list of enter times at each node
		self.count=1		# no:of paths covered 
		self .active=1

		# current_road stores current path nodes
		self.current_road=(path.item(0),path.item(1))

		# exit time of present path
		self.exit=time

		# updates exit time
		self.update_exit()
		self.size=path.shape

	def update(self):

		# checks if exit time of present path is time of environment
		if(self.exit==s.time):

			# Decrease no:of vehicles in curr path by 1
			s.road[self.current_road[0]][self.current_road[1]]-=1

			# Enter entry time of next path in list
			(self.enter).append(self.exit)

			# inc path count by 1
			self.count+=1

			# Check if all paths are covered 
			if self.count<self.size[1]:
				y=self.path

				# update current path nodes
				self.current_road=(y.item(self.count-1),y.item(self.count))

				# update exit time of curr path of vehicle
				self.update_exit()

			else:self.active=0 # if all paths are covered make it inactive

	def update_exit(self):

		# get no:of vehicles in curr path
		x=s.road[self.current_road[0]][self.current_road[1]]

		# calculate speed
		self.speed=(math.exp(0.5*x)+15)/(1+math.exp(0.5*x))

		# calculate exit time
		self.exit=self.exit+(r[self.current_road[0]].item(self.current_road[1])/self.speed)

		# inc no:of vehicles in curr path by 1
		s.road[self.current_road[0]][self.current_road[1]]+=1


(m,n)=t.shape
s=environment()
l=[]	# list of vehices present
i=0

# This loops run util all vehicles enters
while i<m:
	# entry time of next vehicle
	current_time=(t[i].item(0))/60.0

	# update time of environment(s)
	s.update_time(current_time)

	# check if it is time for next vehicle entry
	if current_time==s.time:
		# create new agent i.e for vehicle
		vehicle=agent(v[i],current_time)

		# add it to list
		l.append(vehicle)
		i+=1
		continue

	for j in l:
		if(j.active==1):
			j.update()

flag=True

# This loop runs enter untill all vehices become inactive
while flag:
	s.update_time(150000)
	flag=False
	for j in l:
		if(j.active==1):
			flag=True
			j.update()

# Print the result
for i in l:
	print(i.enter)

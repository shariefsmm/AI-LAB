class environment:
	def __init__(self,shore,location):
		self.shore=shore
		self.current_location=location
	def is_shore(self):
		if(e.current_location==self.shore): return 1
		else: return 0

class bunny:
	def __init__(self,e):
		self.count=0
		self.action='R'
		self.run(e)
	def print_details(self,e):
		print(e.current_location,self.count,e.is_shore(),self.action,e.shore)
	def Action(self,e):
		if(self.action=='R'):
			e.current_location+=self.count
			self.action='L'
		elif(self.action=='L'):
			e.current_location-=self.count
			self.action='R'
	def run(self,e):
		while(1):
			if(e.is_shore()==1):
				self.action=0
				self.print_details(e)
				break
			self.print_details(e)
			self.count+=1
			self.Action(e)
			
			
print("Currentlocation BunnyState Percept Action Truelocation")
e=environment(10,15)
b=bunny(e)


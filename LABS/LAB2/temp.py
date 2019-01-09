class rey:
	def __init__(self,x):
		self.x=x
	def fun(self,p):
		d=p
		print(d)

l=[]
for i in range(10):
	x=rey(i)
	l.append(x)
for i in l:
	print(i.x)
l[0].fun(111)
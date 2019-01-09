import numpy as np
import math as mat
import time

l=10

x=mat.ceil(l/2.0)
print("\t1-Dimensional")
print("X-coordinate","Action")
count=0
start=time.time()
while x!=l:
	action=np.random.randint(2)
	count+=1
	if(action==0):
		if(x!=0):
			# print("%7d %14s"%(x,"Left"))
			print(x,"Left")
			x-=1
		else:print(x,"Stay")
	if(action==1):
		# print("%7d %15s"%(x,"Right"))
		print(x,"Left")
		x+=1
end=time.time()

print("Goal state reached")
print("No:of steps are:%d"%(count))
print("Time taken in seconds is:",(end-start)*100)
print("\n\n")

print("\t2-Dimensional")
print("X-coordinate","Y-coordinate","Action")
x=mat.ceil(l/2.0)
y=mat.ceil(l/2.0)
count=0
start=time.time()
while (x!=l or y!=l):
	action=np.random.randint(4)
	count+=1
	if action==0:
		if(x!=0):
			# print("%7d %14d %14s"%(x,y,"Left"))
			print(x,y,"Left")
			x-=1
		else: print(x,y,"Stay")
	if action==1:
		if(x!=l):
			# print("%7d %14d %15s"%(x,y,"Right"))
			print(x,y,"Right")
			x+=1
		else: print(x,y,"Stay")
	if action==2:
		if(y!=0):
			# print("%7d %14d %14s"%(x,y,"Down"))
			print(x,y,"Down")
			y-=1
		else: print(x,y,"Stay")
	if action==3:
		if(y!=l):
			# print("%7d %14d %14s"%(x,y,"Up"))
			print(x,y,"Up")
			y+=1
		else: print(x,y,"Stay")
end=time.time()

print("Goal state reached")
print("No:of steps are:%d"%(count))
print("Time taken in seconds is:",(end-start)*100)
print("\n\n")

print("\t3-Dimensional")
print("X-coordinate","Y-coordinate","Action")
x=mat.ceil(l/2.0)
y=mat.ceil(l/2.0)
z=mat.ceil(l/2.0)

start=time.time()
count=0
while (x!=l or y!=l or z!=l):
	action=np.random.randint(6)
	count+=1
	if action==0:
		if(x!=0):
			# print("%7d %14d %14s"%(x,y,"Left"))
			print(x,y,z,"Left")
			x-=1
		else: print(x,y,z,"Stay")
	if action==1:
		if(x!=l):
			# print("%7d %14d %15s"%(x,y,"Right"))
			print(x,y,z,"Right")
			x+=1
		else: print(x,y,z,"Stay")
	if action==2:
		if(y!=0):
			# print("%7d %14d %14s"%(x,y,"Down"))
			print(x,y,z,"Down")
			y-=1
		else: print(x,y,z,"Stay")
	if action==3:
		if(y!=l):
			# print("%7d %14d %14s"%(x,y,"Up"))
			print(x,y,z,"Up")
			y+=1
		else: print(x,y,z,"Stay")
	if action==4:
		if(z!=0):
			# print("%7d %14d %14s"%(x,y,"Up"))
			print(x,y,z,"Back")
			z-=1
		else: print(x,y,z,"Stay")
	if action==5:
		if(z!=l):
			# print("%7d %14d %14s"%(x,y,"Up"))
			print(x,y,z,"Front")
			z+=1
		else: print(x,y,z,"Stay")

end=time.time()

print("Goal state reached")
print("No:of steps are:%d"%(count))
print("Time taken in seconds is:",(end-start)*100)
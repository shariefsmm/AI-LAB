import numpy as np
import math as mat
# import mathplot as plt
# plt.plot(10,11)

g=[]
for l in range(1,11):
	x=mat.ceil(l/2.0)
	count=0
	while x!=l:
		action=np.random.randint(2)
		count+=1
		if(action==0):
			if(x!=0):
				# print("%7d %14s"%(x,"Left"))
				# print(x,"Left")
				x-=1
			# else:print(x,"Stay")
		if(action==1):
			# print("%7d %15s"%(x,"Right"))
			# print(x,"Left")
			x+=1
	g.append(count)
print(g)
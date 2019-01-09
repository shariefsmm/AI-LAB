import numpy as np
import math
import matplotlib.pyplot as plt
# np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})

# no:of arms
k=np.random.randint(5,7)

# generating probabilities
f=[]
for _ in range(0,k):
	x=np.random.uniform(0,1)
	f.append(x)

print("MEANS OF {} ARMS ARE AS FOLLOWS:".format(k))
for i in range(0,k):
	print(f[i])

print("HIGHEST MEAN IS OF ARM {}".format(np.argmax(f)))
# pulling each arm once
s=[]
n=[]
for i in range(0,k):
	x=np.random.binomial(1,f[i])
	s.append(x)
	n.append(1)

ITR=100
# plt.set_xlim(1.5,3)
# plt.set_ylim(0,100)
plt.xlim(1.5,3)
plt.ylim(k,ITR)
# plt.axis([1.5,3,0.100])
color=['r','g','b','k','c','m','y']
for t in range(k,ITR+1):
	l=[] # stores ucb of present iteration
	for i in range(0,k):
		y=(s[i]/n[i])+math.sqrt((2*math.log(t))/n[i])
		l.append(y)
		plt.plot(y,t,'*',color[i])
	print("UCB OF ARMS IS AS FOLLOWS: ")
	print(l)
	a=np.argmax(l)
	print("ACTION IS {}".format(a))
	s[a]=s[a]+np.random.binomial(1,f[a])
	n[a]=n[a]+1
plt.show()

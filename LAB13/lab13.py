import numpy as np
import matplotlib.pyplot as plt
import math

noise=np.random.choice([-1,1],1000)

noise=np.array(noise)
theta1=np.zeros(noise.shape)
T=np.zeros(noise.shape)
for t in range(1,1000):
	s=np.sum(noise[:t])
	theta1[t]=s/t
	T[t]=t
s=np.sqrt(T)
plt.figure(1)
plt.plot(T,theta1)
plt.plot(T,1/s)
plt.plot(T,-1/s)


	
theta2=np.zeros(noise.shape)
for t in range(1,1000):
	alpha=1/t
	theta2[t]=theta2[t-1]+(alpha*(noise[t]-theta2[t-1]))
fig2=plt.figure(2)
plt.plot(T,theta2,label='aplha=1/t')


theta3=np.zeros(noise.shape)
for t in range(1,1000):
	alpha=1/(t+100)
	theta3[t]=theta3[t-1]+(alpha*(noise[t]-theta3[t-1]))
fig2=plt.figure(2)
plt.plot(T,theta3,label='alpha=1/(t+100)')



diff=np.zeros(noise.shape)
diff=theta2-theta3
fig2=plt.figure(2)
plt.plot(T,diff,label='diff')
plt.legend()
# plt.legend(,("alpha=1/t","aplha=1/t+1","difference"))


def cal(alpha):
	for t in range(1,1000):
		theta[t]=theta[t-1]+(alpha*(noise[t]-theta[t-1]))


count=3
for (i,color) in [(2,'r'),(1,'b'),(0.1,'g'),(0.01,'y')]:
	theta=np.zeros(noise.shape)
	cal(i)
	fig3=plt.figure(count)
	count+=1
	plt.plot(T,theta)

plt.show()

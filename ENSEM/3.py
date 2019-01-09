
import numpy as np
import math as mat
from scipy.stats import poisson
# poission.pmf(k,Lambda)
V=np.zeros((20,10,10))
R=np.zeros((20,10,10),dtype='float32')
LambdaL=[3,2,2]
LambdaR=[3,1,1]
P=np.zeros((20,10,10))
Action=[1,2,3,4,5]
gamma=0.9

def Get_reward():
	sum1=0
	sum2=0
	sum3=0
	for i in range(20):
		sum1=0
		# print(i)
		for temp in range(i+1):
			sum1=sum1+poisson.pmf(temp,LambdaL[0])
		# print(sum1)
		for j in range(10):
			sum2=0
			for temp in range(j+1):
				sum2=sum2+poisson.pmf(temp,LambdaL[1])
			for k in range(10):
				sum3=0
				for temp in range(k+1):
					sum3=sum3+poisson.pmf(temp,LambdaL[0])
			# print(sum1,sum2,sum3,(sum1+sum2+sum3)*10)
				R[i][j][k]=(sum1+sum2+sum3)*10
			# if(R[i][j][k]!=0 and k!=9):print(R[i][j][k])


Get_reward()
# print(R)

def find(i,j,k,a,P):
	x=y=z=0
	temp=0
	cost=0
	c=0
	count=0
	total=0.0
	for x in range(20):
		for y in range(10):
			for z in range(10):
				count=abs(x-i)+abs(y-j)+abs(z-k)
				count=count/2
				error1=y-j
				error2=z-k
				correction=0
				if error1*erro2<0:correction=min(abs(error1),abs(error2))
				if count==a:
					total+=1
					cost=-2*count + 2*correction
					if cost>0 : print(cost)
					temp=temp+P[x][y][z] +cost
				# if i==16 and j==6 and k==9:
				# 	print("temp is ",temp)
					# for t1 in range(x+1,20):
					# 	sum1=0
					# 	for temp in range(t1-x):
					# 		sum1=sum1+poisson.pmf(temp,LambdaR[0])
					# 	for t2 in range(y+1,10):
					# 		sum2=0
					# 		for temp in range(t2-y):
					# 			sum2=sum2+poisson.pmf(temp,LambdaR[1])
					# 		for t3 in range(z+1,10):
					# 			sum3=0
					# 			for temp in range(t3-z):
					# 				sum3=sum3+poisson.pmf(temp,LambdaR[1])
					# 			temp=temp+(sum1*sum2*sum3)*P[t1][t2][t3]
	return (temp)/total


def value_iteration():
	print("Value_iteration started")
	itr=0;
	while(1):
		itr+=1
		print("Iteration number is ",itr)
		threshold=-1
		Prev=V.copy()
		for i in range(20):
			for j in range(10):
				for k in range(10):
					l=[]
					for a in Action:
						# print("went")
						temp=find(i,j,k,a,Prev)
						# print('out')
						l.append(R[i][j][k]+gamma*temp)
					V[i][j][k]=np.max(l)
					P[i][j][k]=np.argmax(l)
					if abs(V[i][j][k]-Prev[i][j][k])>threshold:value=[i,j,k]
					threshold=max(threshold,abs(V[i][j][k]-Prev[i][j][k]))
		# print("after change")
		# print(V)
		# print("before change")
		# print(Prev)
		print(value)
		print(V[value[0]][value[1]][value[2]],Prev[value[0]][value[1]][value[2]])
		if threshold<=0.1:break
		print("Threshold ",threshold)

	print("value_iteration completed")
	print("values")
	print(V)
	print("policy")
	print(P)


value_iteration()

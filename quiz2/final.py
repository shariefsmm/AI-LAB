import numpy as np
r=[3.0,3.5,4,4.5,5]
pw=[1.0/33.0,1.0/30.0,1.0/24.0,1.0/18.0,1.0/15.0]

v=np.zeros(11*4,dtype='float').reshape(11,4)
# policy=np.zeros(11*4,dtype='int').reshape(11,4)
policy=[[-1 for i in range(4)]for j in range(11)]
Final_value=[[-1 for i in range(4)]for j in range(11)]

def verify(t,x,b):
	p=t
	count=0
	if p<=10:
		count=max(count,bowler[p][x][b])
		p+=1
	return count
	# p=t
	# count=0
	# while p<=10:
	# 	count=count+bowler[p][x][b]
	# 	# if count>=2:
	# 	# 	return False
	# 	p+=1
	# # if count>=2:return False
	# return count
def BELLMAN(x,t):
	# l=[0,0,0,0,0]{0:0,1:5,2:15,3:4}
	l={}
	for b in range(0,5,1):
		# (pw,pr)=get_probability(x,a)
		# l[a]=(1-pw)*(pr*r[a]+prev[t-1][x])+(pw)*prev[t-1][x-1]
		y=((1-pw[b]*6))*(prev[t-1][x]+r[b])+(pw[b]*6)*(prev[t-1][x-1]+r[b])
		if y in l:
			l[y+0.00000001]=b
			continue
		l[y]=b
	p=sorted(l)
	n=0
	# print(l)
	# print(p)
	while(n<5):
		b=l[p[n]]
		# print(l)
		# print(p)
		# print(b)
		if x==2:
			c1=verify(t+1,x,b)
			c2=verify(t+1,x+1,b)
			if max(c1,c2)<2:
					bowler[t][x][b]=max(c1,c2)+1
					v[t][x]=p[n]
					policy[t][x]=b
					break
			# else:
			# 	bowler[t][x][b]+=1
			# 	v[t][x]=p[n]
			# 	policy[t][x]=b
			# 	break
		elif x==1:
			c1=verify(t+1,x,b)
			c2=verify(t+1,x+1,b)
			c3=verify(t+2,x+2,b)
			if max(c1,c2,c3)<2:
					bowler[t][x][b]=max(c1,c2,c3)+1
					v[t][x]=p[n]
					policy[t][x]=b
					break
			# else:
			# 	bowler[t][x][b]+=1
			# 	v[t][x]=p[n]
			# 	policy[t][x]=b
			# 	break
		elif x==3:
			c1=verify(t+1,x,b)
			if x==3 and b==0:
				print("hello",t,counter,c1)
			if c1<2:
				bowler[t][x][b]=c1+1
				v[t][x]=p[n]
				policy[t][x]=b
				break
			# else:
			# 	bowler[t][x][b]+=1
			# 	v[t][x]=p[n]
			# 	policy[t][x]=b
			# 	break

		n=n+1
	# v[t][x]=p[0]
	# Final_value[t][x]=p
	# # print(p)
	# b=[l[p[0]],l[p[1]],l[p[2]],l[p[2]],l[p[4]]]
	# # print(b)
	# policy[t][x]=b

	# v[t][x]=p[0]
	# policy[t][x]=r[np.argmax(l)]

counter=0
while(1):
	delta=-1
	prev=v.copy()
	count=[0,0,0,0,0]
	counter+=1
	policy=[[-1 for i in range(4)]for j in range(11)]
	bowler=[[[0 for k in range(5)] for i in range(4)]for j in range(11)]
	for t in range(1,11,1):
		for x in range(1,4,1):
			BELLMAN(x,t)
			delta=max(delta,abs(prev[t][x]-v[t][x]))
	if delta<0.01:break	

print("Optimal batting policy is:")
for t in range(1,11,1):
		print("No:of overs left:{}".format(t))
		for x in range(1,4,1):
			print(policy[t][x],end=" ")
		print(" ")
# print(Final_value[1][3])
for i in range(1,11,1):
	print(bowler[i][3][0])
print("Expected runs acctording to policy is:")
for t in range(1,11,1):
	print("No:of overs left:{}".format(t))
	print(v[t])
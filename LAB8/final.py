import numpy as np

n=3
(X,Y)=(n-1,n-1)
goal=n**2-1
gamma=[0.01,0.9,0.99,0.999]
up = 0
down = 1
left = 2
right = 3
print("Goal-state:bottom_right")
d={0:'up',1:'down',2:'left',3:'right'}
l=np.zeros(n**2,dtype='float').reshape(n**2,1)

R=[l.copy(),l.copy(),l.copy(),l.copy()]
v=l.copy()
l=np.zeros(n**4,dtype='float').reshape(n**2,n**2)
P=[l.copy(),l.copy(),l.copy(),l.copy()]
p_c=0.8
p_w=1-p_c
r=np.zeros(n*n,dtype='float').reshape(n,n)
r[X][Y]=1
r[1][1]=-1
def update(action,s,p):
	if s-n>=0:
		if P[action][s][s-n]==0.0:
			P[action][s][s-n]=p
	else: P[action][s][s]=p
	if s+n<n**2:
		if P[action][s][s+n]==0.0:
			P[action][s][s+n]=p
	else: P[action][s][s]=p

	if (s+1)//n==(s//n):
		if P[action][s][s+1]==0.0:
			P[action][s][s+1]=p
	else: P[action][s][s]=p

	if (s-1)//n==(s//n):
		if P[action][s][s-1]==0.0:
			P[action][s][s-1]=p
	else: P[action][s][s]=p

def PROB():
	for s in range(n**2):
		t=0
		if s-n>=0:t+=1
		if s+n<n**2:t+=1
		if (s+1)//n==(s//n):t+=1
		if (s-1)//n==(s)//n:t+=1
		if t!=4:t+=1
		# print(s,t)
		if s-n>=0:
			P[up][s][s-n]=p_c
			t_w=p_w/(t-1)
			# print(t_w)
			update(up,s,t_w)

		# for down
		if s+n<n**2:
			P[down][s][s+n]=p_c
			t_w=p_w/(t-1)
			update(down,s,t_w)

		# for right
		if (s+1)//n==(s//n):
			P[right][s][s+1]=p_c
			t_w=p_w/(t-1)
			update(right,s,t_w)

		# for left
		if (s-1)//n==(s//n):
			P[left][s][s-1]=p_c
			t_w=p_w/(t-1)
			update(left,s,t_w)

def GetReward():
	for s in range(n**2):
		for i in [up,down,left,right]:
			for j in range(n**2):
				x=j//n
				y=j%n
				R[i][s]+=P[i][s][j]*r[x][y]


PROB()
GetReward()
def Print():
	print("up")
	print(R[0])
	print("down")
	print(R[1])
	print("left")
	print(R[2])
	print("right")
	print(R[3])

	print("up")
	print(P[0])
	print("down")
	print(P[1])
	print("left")
	print(P[2])
	print("right")
	print(P[3])

# Print()

# Value-iteration
def ValueItr(gamma):
	V=v.copy()
	l=[0,0,0,0]
	delta=0
	while(1):
		prev=V.copy()
		delta=0
		for s in range(n**2):
			for i in [up,down,right,left]:
				l[i]=R[i][s][0]+gamma*np.dot(P[i][s],prev)[0]
			V[s]=max(l)
			delta=max(delta,abs(prev[s][0]-V[s][0]))
		if delta<0.01:break
	V_policy=[]
	for s in range(n**2):
		for i in [up,down,right,left]:
			l[i]=R[i][s][0]+gamma*np.dot(P[i][s],V)
		V_policy.append(d[np.argmax(l)])

	print("Optimal policy based on Value-iteration for gamma=%f"%(gamma))
	print(np.array(V_policy).reshape(n,n))

# Policy iteration
def PolicyItr(gamma):
	V=v.copy()
	policy=np.zeros(n**2,dtype="int").reshape(n**2,1)
	flag=1
	l=[0,0,0,0]
	while(flag==1):
		flag=0
		prev=V.copy()
		for s in range(n**2):
			V[s]=R[policy[s][0]][s][0]+gamma*np.dot(P[policy[s][0]][s],prev)[0]
		for s in range(n**2):
			for i in [up,down,right,left]:
				l[i]=R[i][s][0]+gamma*np.dot(P[i][s],V)[0]
			if policy[s][0]!=np.argmax(l):
				policy[s][0]=np.argmax(l)
				flag=1
	P_policy=[]
	for s in range(n**2):
		P_policy.append(d[policy[s][0]])
	print("Optimal policy based on Policy-iteration for gamma=%f"%(gamma))
	print(np.array(P_policy).reshape(n,n))

for g in gamma:
	ValueItr(g)
	PolicyItr(g)

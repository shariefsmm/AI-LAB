import numpy as np
import math 
import matplotlib.pyplot as plt
V=[-0.07,0.007]
P=[-1.2,0.6]
bins=20

Velocity=np.linspace(-0.07,0.007,bins)
Position=np.linspace(-1.2,0.6,bins)

vr=(V[1]-V[0])/(bins-1)
pr=(P[1]-P[0])/(bins-1)

d={0:'left',1:'neutral',2:'right'}
left=0
neutral=1
right=2
Action=[-1,0,1]

# grid=np.zeros(bins*bins).reshape(bins,bins)
# v=np.zeros(bins*bins,dtype='float32')
def get_coordinates(s):
	x=s//bins;
	y=s%bins;
	return (x,y)

def convert_coordinates(position,velocity):
	x=int(np.ceil((position-P[0])/pr))
	y=int(np.ceil((velocity-V[0])/vr))
	s= x*bins + y
	return s

def Update_function(a,s):
	(x,y)=get_coordinates(s)
	vel=Velocity[y]
	pos=Position[x]

	done=False
	r=0
	velocity=vel+(Action[a]*0.001)+ math.cos(3*pos)*(-0.0025)
	position=pos+velocity
	# if s==16:print(position,velocity)
	if position<P[0]:
		position=P[0]
		velocity=V[0]
	# if velocity<V[0]:velocity=V[0]

	if position>=P[1]:
		position=P[1]
		velocity=V[1]
		# print("hello")
		r=1
		done=True
	if velocity>V[1]:velocity=V[1]
	next_state=convert_coordinates(position,velocity)
	# if s==16:print(position,velocity,next_state)

	return (r,next_state)

# value_iteration
def value_iteration():
	v=np.zeros(bins*bins,dtype='float32')
	value=v.copy()
	reward=[v.copy(),v.copy(),v.copy(),v.copy()]
	v=np.zeros(bins*bins,dtype='int32')
	prob=[v.copy(),v.copy(),v.copy()]
	for s in range(bins*bins):
		for a in [left,neutral,right]:
			(reward[a][s],prob[a][s])=Update_function(a,s)
	l=[0,0,0]
	gamma=0.9
	k=0	
	for it in range(100):
		# print(it)
		delta=0
		prev=value.copy()
		for s in range(bins*bins):
			for a in [left,neutral,right]:
				# (r,ns)=Update_function(a,s)
				# l[a]=r+gamma*prev[ns]
				l[a]=reward[a][s]+gamma*prev[prob[a][s]]
				# if s==16:
				# 	print("hello",l,prob[a][s],a)
			value[s]=max(l)
			delta=max(delta,abs(prev[s]-value[s]))
		if delta<0.01:break
	policy=[]
	for s in range(bins*bins):
		for a in [left,neutral,right]:
			# (r,ns)=Update_function(a,s)
			# l[a]=r+gamma*prev[ns]
			l[a]=reward[a][s]+gamma*value[prob[a][s]]
		policy.append(d[np.argmax(l)])
	# for s in range(bins*bins):
	# 	print(s,value[s])
	print("Optimal policy based on value-iteration for gamma=%f"%(gamma))
	print(np.array(policy).reshape(bins,bins))
	Final_value=value.reshape(bins,bins)
	# print(Final_value)
	plt.imshow (Final_value , cmap = "hot" , interpolation='nearest')
	plt.show()

# policy_iteration
def policy_iteration():
	v=np.zeros(bins*bins,dtype='float32')
	value=v.copy()
	reward=[v.copy(),v.copy(),v.copy(),v.copy()]
	v=np.zeros(bins*bins,dtype='int32')
	prob=[v.copy(),v.copy(),v.copy()]
	for s in range(bins*bins):
		for a in [left,neutral,right]:
			(reward[a][s],prob[a][s])=Update_function(a,s)
	l=[0,0,0]
	gamma=0.9
	flag=1
	v=np.zeros(bins*bins,dtype='int')
	policy=v.copy()
	# print("hello",policy[0])
	while(flag==1):
		flag=0
		prev=value.copy()
		for s in range(bins*bins):
			# (r,ns)=Update_function(policy[s],s)
			# value[s]=r+gamma*prev[s]
			value[s]=reward[policy[s]][s]+gamma*prev[prob[policy[s]][s]]
		for s in range(bins*bins):
			for a in [left,neutral,right]:
				(r,ns)=Update_function(a,s)
				l[a]=r+gamma*ns
			if policy[s]!=np.argmax(l):
				policy[s]=np.argmax(l)
				flag=1
	P_policy=[]
	for s in range(bins*bins):
		P_policy.append(d[policy[s]])
	print("Optimal policy based on Policy-iteration for gamma=%f"%(gamma))
	print(np.array(P_policy).reshape(bins,bins))


value_iteration()
policy_iteration()



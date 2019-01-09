import numpy as np
r=[1,2,3,4,6]
def get_probability(x,a):
	pw_min=[0.01,0.02,0.03,0.1,0.3]
	pw_max=[0.1,0.2,0.3,0.5,0.7]
	pw=pw_max[a] +(pw_min[a]-pw_max[a])*((x-1)/9.0)

	pr_min=0.5
	pr_max=0.8
	pr=pr_min+(pr_max-pr_min)*((x-1)/9.0)

	return (pw,pr)

def BELLMAN(x,t):
	l=[0,0,0,0,0]
	for a in range(5):
		(pw,pr)=get_probability(x,a)
		l[a]=(1-pw)*(pr*r[a]+prev[t-1][x])+(pw)*prev[t-1][x-1]
	v[t][x]=np.max(l)
	policy[t][x]=r[np.argmax(l)]

v=np.zeros(11*301,dtype='float').reshape(301,11)
policy=np.zeros(11*301,dtype='int').reshape(301,11)
count=0
while(1):
	delta=-1
	prev=v.copy()
	for t in range(1,301,1):
		for x in range(1,11,1):
			BELLMAN(x,t)
			delta=max(delta,abs(prev[t][x]-v[t][x]))
	if delta<0.01:break
	
print("Optimal batting policy is:")
for t in range(1,301,1):
		print("No:of balls left:{}".format(t))
		print(policy[t])

print("Expected runs acctording to policy is:")
for t in range(1,301,1):
		print(v[t])
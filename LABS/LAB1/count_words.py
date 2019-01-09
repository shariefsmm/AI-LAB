count=0
active=0
f=open("test.txt",'r')
while 1:
	x=f.read(1)
	if x=='':
		if active==1:
			count+=1
		break
	if x!=' ' and x!='\n':active=1
	if x==' ' and active==1:
		count+=1
		active=0
	#if x==' ' and active==0:active=0
print(count)



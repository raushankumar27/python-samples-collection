while(True):
	n=int(input())
	if(n==-1):
		break
	temp=n
	box=[]
	while(temp>0):
		temp-=1
		box.append(int(input()))
	s=sum(box)
	if(s%n!=0):
		print("-1")
	else:
		z=s//n
		s=0
		for i in box:
			if(i>z):
				s+=(i-z)
		print(s)
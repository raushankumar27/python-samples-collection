for t in range(int(input())):
	n=input()
	a=list(map(int,input().split()))
	#print(a)
	s=1
	p=a[0]
	i=1
	for x in a[1:]:
		if(x>=p):
			i=i+1
		else:
			i=1
		s=s+i
		p=x
	print(s)

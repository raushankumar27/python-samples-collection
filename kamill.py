i=10
while(i>0):
	i-=1
	s=input()
	z=['L','T','D','F']
	p=1
	for x in s:
		if x in z:
			p*=2
	print(p)
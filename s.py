for x in range(1000,9999,1):
	z=x*4
	s1=str(z)
	s2=str(x)
	s2=s2[::-1]
	if s1==s2:
		print(x)
		break
t=int(input())
while(t>0):
	t-=1
	n=int(input())
	z=n/5
	i=5
	c=0
	while(z>0):
		z=n//i
		c+=z
		i*=5
	print(c)
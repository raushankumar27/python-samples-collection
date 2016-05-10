while(True):
	n=int(input())
	if(n==0):
		break
	s=input()
	z=[]
	p=0
	l=len(s)
	for x in range(n,l+1,n):
		z.append(s[p:x:])
		p=x
	l=len(z)
	for x in range(1,l,2):
		z[x]=z[x][::-1]
	for i in range(n):
		for j in range(l):
			print(z[j][i],end='')
	print()	
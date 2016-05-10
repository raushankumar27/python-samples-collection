t=int(input())
while(t>0):
	t-=1
	r,c=map(int,input().split())
	s1=""
	s2=''
	for i in range(c):
		if(i%2==0):
			s1+='*'
			s2+='.'
		else:
			s1+='.'
			s2+='*'
	for i in range(r):
		if(i%2==0):
			print(s1)
		else:
			print(s2)
	print()
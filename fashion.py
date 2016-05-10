t=int(input())
while(t>0):
	t-=1
	n=int(input())
	men=list(map(int,input().split()))
	women=list(map(int,input().split()))
	men.sort(reverse=True)
	women.sort(reverse=True)
	s=0
	for i in range(n):
		s+=men[i]*women[i]
	print(s)
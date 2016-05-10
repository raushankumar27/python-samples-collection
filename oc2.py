for t in range(int(input())):
	n=int(input())
	a=input()
	b=input()
	ri=0
	pr=list(map(int,input().split()))
	maxi=pr[0]
	for i in range(n):
		if(a[i]==b[i]):
				ri=ri+1
	if(ri==n):
		maxi=pr[n]
	else:
		maxi=max(pr[:ri+1])
	print(maxi)


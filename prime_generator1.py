def prime_upto(a,b):
	from math import sqrt
	limit=int(sqrt(b))+1
	z=[1 for x in range(limit+1)]
	if(a<2):
		a=2
	ans=[1 for x in range(b-a+1)]
	i=2
	z[0]=0
	z[1]=0
	n=len(z)
	while(i<n):
		if(z[i]==1):
			for x in range(2*i,n,i):
				z[x]=0
		i+=1
	#testing
	#print("z=",z)
	
	ansl=len(ans)
	for x in range(n):
		if z[x]==1:
			if(a%x==0):
				start=0
			else:
				start=x-(a%x)
			if( a+start==x):
				start+=x
			for i in range(start,ansl,x):
				ans[i]=0
			#print(ans)
	#test2
	#print(ans)
	
	for x in range(ansl):
		if(ans[x]==1):
			print(a+x)
			
		

if(__name__=='__main__'):
	t=int(input())
	while(t>0):
		t-=1
		a,b=map(int,input().split())
		prime_upto(a,b)
		print()
	
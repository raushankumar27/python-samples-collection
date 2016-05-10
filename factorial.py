def fac(n):
	ans=1
	for i in range(2,n+1):
		ans*=i
	return ans

if(__name__=='__main__'):
	t=int(input())
	while(t>0):
		t-=1
		n=int(input())
		print(fac(n))
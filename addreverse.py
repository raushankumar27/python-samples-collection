
def rt0(a):
	al=len(a)
	for i in range(al):
		if(a[i]!='0'):
			a=a[i:]
			#print('reversed',a)
			return a

if(__name__=='__main__'):
	t=int(input())
	while(t>0):
		t-=1
		a,b=map(str,input().split())
		a=rt0( a[::-1])
		b=rt0(b[::-1])
		a=int(a)
		b=int(b)
		s=a+b
		s=str(s)
		s=rt0(s[::-1])
		print(s)
		
		
		
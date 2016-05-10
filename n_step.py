t=int(input())
while(t>0):
	t-=1
	x,y=map(int,input().split())
	#check valid co-ordinate
	if(y==x or x-y==2):
		if(x%2==1):
			print(x+y-1)
		else:
			print(x+y)
	else:
		print('No Number')
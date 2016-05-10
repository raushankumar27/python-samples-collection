t=int(input())
while(t>0):
	t-=1
	r,c=map(int,input().split())
	fl='*'*c
	ml=''
	if(c<3):
		ml='*'*c
	else:
		ml='*'+'.'*(c-2)+'*'
	if(r>=1):
		print(fl)
	for x in range(3,r+1):
		print(ml)
	if(r>=2):
		print(fl)
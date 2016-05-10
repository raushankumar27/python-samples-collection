t=int( input() )
while(t>0):
	t-=1
	s=input()
	level={'+':1,'-':2,'*':3,'/':4,'^':5}
	bc={')':'(','}':'{',']':'['}
	opb=['(','{','[']
	clb=list( bc.keys()  )
	#print(clb)
	st=[]
	z=list(level.keys())
	for x in s:
		#print(st)
		#print("found ",x)
		
		if x in clb:
			while(st!=[] and st[-1]!=bc[x] ):
				print(st.pop(),end='')
			st.pop()
		
		elif x in z:
			if len(st)==0:
				st.append(x)
			elif level.get(st[-1],0)<=level[x]:
				st.append(x)
			else:
				p=st[-1]
				while(level[st[-1]]>level[x]):
					print(st[-1],end='')
					st.pop()
		elif x in opb:
			st.append(x)
		else:
			print(x,end='')
	while st:
		print(st.pop(),end='')
	print()
		
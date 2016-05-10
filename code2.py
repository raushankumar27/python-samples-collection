for t in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	#print(a)
	st=[]
	for num in a:
		for i,z in enumerate(st):
			if num<z:
				st[i]=num
				#st.sort()
				#print('after replacing',st)
				break
		else:
			st.append(num)
			#print('after adding',st)
			#st.sort()
			

	print(len(st),end=' ')
	for x in st:
		print(x,end=' ')
	print('')

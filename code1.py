for t in range(int(input())):
	n,k=map(int,input().split())
	lisn=[]
	listk=[]
	lisn=input().split()
	#print(lisn)
	for z in range(k):
		x=input().split()
		del x[0]
		listk.append(x)
	#print (listk)
	
	for x in lisn:
		r=0
		#print('taking '+ x)
		for ph in listk:
			#print('sending',ph)
			for z in ph:
				#print("comparing with "+z)
				if z==x:
					print("YES",end=' ')
					r=1
					break
			if r==1:
				break
		else:
			print("NO",end=' ')
	print('')
	
	
			

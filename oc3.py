for t in range(int(input())):
	a=float(input())
	if(a==180):
		print("06:00")
	if(a==0):
		print("00:00")
	else:
		for h in range(12):
			for m in range(60):
				#print((30*h+0.5*m)%180-6*m)
				if(abs((30*h+0.5*m)-6*m)==a):
					print("%02d:%02d"%(h,m))
	


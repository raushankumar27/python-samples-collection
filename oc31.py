for t in range(int(input())):
	a=float(input())
	if(a==180):
		print("06:00")
	if(a==0):
		print("00:00")
	else:
		for h in range(6):
			for m in range(30):
				if(abs((30*h+0.5*m)-6*m-a)<=1/120):
					print("%02d:%02d"%(h,m))
					if(m==0):
						print("%02d:%02d"%(12-h,(0)))
					else:
						print("%02d:%02d"%(12-h-1,(60-m)))
					break
	



def perm(s):
	out=[]
	if(len(s)<=1):
		out.append(s)
		return out
	else:
		for i,lett in enumerate(s):
			for x in perm(s[:i:]+s[(i+1)::]):
				out+=[lett+x]
		return out
		
if(__name__=='__main__'):
	s=input()
	print(perm(s))
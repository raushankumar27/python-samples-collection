def toh(n,s,d,a):
    if(n==0):
        print("move ",s," to",d)
    else:
        toh(n-1,s,a,d)
        print("move ",s,d)
        toh(n-1,a,d,s)
toh(24,"a","b","c")

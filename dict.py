for t in range(input()):
    n,m=map(int,raw_input().split())
    l,r,c,p,q,s=map(int,raw_input().split())
    cost=[0 for x in range(n)]
    if(m==1):
        print l,c
    else:
        for mi in range(m):
            for i in range(l,r+1):
                cost[i-1]+=c
            l = (l * p + r) % n + 1;
            r = (r * q + l) % n + 1;
            if(l > r):
                t=l
                l=r
                r=t
            c=(c*s)%1000000 + 1;
        ma=max(cost)
        for x in range(n):
            if(cost[x]==ma):
                print x+1,ma
                break

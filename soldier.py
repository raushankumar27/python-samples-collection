n,m=map(int,input().split())
e=list(map(int,input().split()))
e.insert(0,0)
P=[0 for x in range(n+1)]
P[1]=1
for x in range(n-1):
    u,v=map(int,input().split())
    P[v]=u

A=[[] for x in range(n+1)]
for i in range(1,n+1):
    A[i].append(i)
for i in range(2,n+1):
    j=i
    while(j!=1):
        A[P[j]].append(i)
        j=P[j]
while(m>0):
    m-=1
    S=list(input().split())
    if(S[0]=='Q'):
        u=int(S[1])
        l=len(A[u])
        s=0
        for j in range(l):
           s+=e[A[u][j]]
        print(s)
    else:
        u=int(S[1])
        v=int(S[2])
        e[u]=v
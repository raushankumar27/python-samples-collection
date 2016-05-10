#require recheck
t=int(input())
while(t>0):
    t-=1
    a=list(map(int,input().split()))
    z=(a[0]**a[1])%a[2]
    print(z)
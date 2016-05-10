t=int(input())
while(t>0):
    t-=1
    n=list(map(int,raw_input().split()))
    arrival=map(int,raw_input().split())
    c=0
    for x in arrival:
        if(x<=0):
            c+=1
        if(c>=n[1]):
            print("NO")
            break
    if(c<n[1]):
        print("YES")
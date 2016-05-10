t=int(input())
while(t>0):
    t-=1
    n=int(input())
    lrem=n%4
    if(lrem==1 or lrem==3 or lrem==0):
        print("Yes")
    else:
        print("No")
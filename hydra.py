t=int(input())
while(t>0):
    t-=1
    s=input()
    zd={}
    for x in s:
        pc=zd.get(x,0)
        zd[x]=pc+1
    p=zd.keys()
    #print(p)
    flag=0
    for x in p:
        num=ord(x)-96
        if(not num==zd[x]):
            print("S.H.I.E.L.D")
            flag=1
            break
    if(flag==0):
        print("HYDRA")
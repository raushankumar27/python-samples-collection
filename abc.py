t=int(input())
while(t>0):
    t-=1
    a=input()
    try:
        s=0
        a=map(int,a.split())
        for x in a:
            s+=x
        print(s)
    except:
        print("Invalid Input")
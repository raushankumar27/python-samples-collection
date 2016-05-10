#tcs ant one can code solution
f=input()
f1=open(f,'r')
t=f1.readline()
t=int(t)
while(t>0):
    t-=1
    try:
        a=f1.readline()
        z=map(int,a.split())
        s=0
        for x in z:
            s+=x
        print(s)
    except:
        print("Invalid Input")
f1.close()

import math
te=int(input())
while(te>0):
    te-=1
    a,H,t=map(int,input().split())
    if(t==0):
        print(H)
    else:
        z=math.tan(math.radians(t))
        if(z<=H/a):
            hei=a*z
            rem_height=((H*a)-(0.5*a*hei))/a
        else:
            rem_base=H/z
            print(rem_base)
            rem_height=(0.5*rem_base*H)/a
        print(math.ceil(rem_height))

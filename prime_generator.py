prcol=[2,3,5,7,11]

def prime_check(n):
    if(n<2):
        return False
    if(n==2):
        return True
    if(n%2==0):
        return False
    from math import sqrt
    z=int(sqrt(n))+1
    for i in prcol:
        if(n%i==0):
            return False
        if(i>n):
            break
    return True

if(__name__=='__main__'):
    t=int(input())

    
    while(t>0):
        t-=1
        a,b=map(int,input().split())
        for x in prcol:
            if(x>=a and x<=b):
                print('fl',x)
            if(x>b):
                break
        
        for x in range(prcol[-1],b+1):
            if(prime_check(x)):
                prcol.append(x)
                print('gen',x)
        print()
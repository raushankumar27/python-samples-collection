for x in range(int(input())):
    a=[0 for x in range(26)]
    s1=input()
    s2=input()
    flag=0
    for i in s1:
        a[ord(i)-97]+=1
    
    for i in s2:
        p=ord(i)-97
        if( a[p] >= 1):
            flag=1
            break
        
    if(flag==1):
        print("Yes")
    else:
        print("No")


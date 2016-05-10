import re
t=int(input())
while(t>0):
    t-=1
    s1=input()
    s2=input()
    s3=input()
    s4=input()
    mp=[]
    for x in range(1,len(s1)):
        for j in range(len(s1)-x):
            q=s2.find(s1[j:j+x])
            mp.append(s2[q:q+x])
    print(mp)
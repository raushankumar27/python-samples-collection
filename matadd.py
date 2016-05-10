m1=input()
m2=input()
ma1=open(m1,'r')
ma2=open(m2,'r')
z1=[]
z2=[]
try:
    for x in ma1:
        x=map(int,x.split())
        z1.append(list(x))
    for x in ma2:
        x=map(int,x.split())
        z2.append(list(x))
    ma1.close()
    ma2.close()
    #printing 1st matrix
    print("Input Matrix 1 :")
    for x in z1:
        print("".join(x))
    #printing second matrix
    print("Input Matrix 2 :")
    for x in z2:
        for y in x:
            print(y,end='')
        print(" ")
    #valid matix check
    if(len(z1)==len(z2) and len(z1[0])==len(z2[0]) ):
        ro=len(z1)
        co=len(z1[0])
        ans=[]
        print("Valid Matrix dimensions for addition.")
        for i in range(ro):
            p=[]
            for j in range(co):
                print(z1[i][j]+z2[i][j],end=' ')
            print()
    else:
        print("Invalid Matrix dimensions for addition.")
        print("Cannot add matrix of dimensions {}x{} with {}x{}".format(len(z1),len(z1[0]),len(z2),len(z2[0])    ))

except:
    print("INVALID INPUT")
import time

print("gvhfd")
f=open("ques.txt","r+")
print("sgrg")
n=int(f.readline())
print("number of question %d"%n)

while(n>0):
    n-=1
    f.readline()
    ty=int(f.readline())
    print("type=",ty,'\n')
    ques=f.readline()
    print(ques)
    if(ty==0):
        for i in range(4):
            print(f.readline())
        print("answer is",f.readline())
    if(ty==1):
        print("answer is",f.readline())
    input()

print("reading complete")
f.close()
#print(n)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



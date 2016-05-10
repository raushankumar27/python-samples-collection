def findCount(self, A, B):
        done=True
        b=len(A)
        a=0
        cou=0
        while(done):
           m=(a+b)//2
           if(A[m]==B):
                done=False
                a=m
                while(A[a]==m):
                    cou+=1
                    a+=1
                a=m
                while(A[a]==m):
                    cou+=1
                    a+=1
            if(a==l-1 or b==0):
                break
            if(A[m]<B):
                a=m
            if(A[m]>B):
                b=m
            
    return cou               

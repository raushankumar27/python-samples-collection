def par_check(s):
    l=len(s)
    if(not l%2==0):
        return(False)
    opening=['(','{','[']
    closing={')':"(",'}':'{',']':'['}
    sts=[]
    for x in s:
        if(x in opening):
            sts.append(x)
        else:
            if(len(sts)==0):
                return(False)
            lastin=sts.pop()
            if(not closing[x]==lastin):
                return False
    return len(sts)==0
    
if(__name__=='__main__'):
    s=input()
    print(par_check(s))
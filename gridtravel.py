def GRID(n, m):
    if(n==m and m%2==0):
        return("L")
    if(m==n and m%2==1):
        return ('R')
    if(m==2 and n>2):
        return("U")
    if(n>m):
        return('D')
print(GRID(5,4))

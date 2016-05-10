def censor(text,word):
    z=list(text.split())
    rep=''
    ret=''
    print(z)
    for x in word:
        rep=rep+'*'
    for x in z:
        if x==word:
            ret=ret+rep
        else:
            ret=ret+x
        ret=ret+' '
    ret.strip()
    return ret

print(censor('Hey Hey Hey','Hey'))

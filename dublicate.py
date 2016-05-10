def remove_duplicates(item):
    print (item)
    z=list(item)
    z.sort()
    print (item)
    print(z)
    r=[]
    r.append(z[0])
    for x in range(1,len(z)):
        if z[x]!=z[x-1]:
            r.append(z[x])
    return r

print(remove_duplicates([4,5,5,4]))

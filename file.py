f1=open("f1.txt","r+")
print(f1.read())
f1.write("wgdugae\n")
try:
    f2=open("f2.txt","r+")
except(Exception):
    from file import f2c
    f2=f2c()
f2.write(f1.read)
print("f2 reading\n",f2.read())

def f2c():
    f2=open("f2.txt","w+")
    return f2
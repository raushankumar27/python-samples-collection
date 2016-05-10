def f2c():
    print("f2 created\n")
    f2=open("f2.txt","w+")
    return f2

f1=open("f1.txt","r+")
print(f1.read())

f1.write("wgdugae\n")
f1.close()
try:
    f2=open("f2.txt","r+")
except(Exception):
    f2=f2c()
f1=open("f1.txt","r+")
z1=f1.read()
f2.write(z1)
print("f2 reading\n")
print(f2.read())
f1.close()
f2.close()


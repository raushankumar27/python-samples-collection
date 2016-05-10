
a=input()
try:
    s=0
    for x in a.split():
        s+=int(x)
    print(s)
except(Exception):
    print("Invalid Input")

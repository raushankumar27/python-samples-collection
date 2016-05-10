from tkinter import *

root=Tk()
mframe=Frame(root,height=700)
iframe=Frame(root,height=700)

qtype=0

def mcqf():
    e=Text(mframe,height=10)
    e.pack()
    o=Label(mframe,text="option 1").pack()
    o1=Entry(mframe).pack()
    o=Label(mframe,text="option 2").pack()
    o2=Entry(mframe).pack()
    o=Label(mframe,text="option 3").pack()
    o3=Entry(mframe).pack()
    o=Label(mframe,text="option 4").pack()
    o4=Entry(mframe).pack()
    o=Label(mframe,text="correct option enter integer").pack()
    ans=Entry(mframe).pack()
    o=Label(mframe,text="done",anchor= 'e').pack()
    #mframe.pack()
    
def intf():
    f1=Label(iframe,text="enter question").pack()
    e1=Text(iframe,height=10).pack()
    f1=Label(iframe,text="enter  correct answer").pack()
    ans=Entry(iframe).pack()
    f1=Label(iframe,text="done").pack()
def mcqframe():
    qtype=0
    b1.state=DISABLED
    b2.state=NORMAL
    iframe.pack_forget()
    mframe.pack()
def intframe():
    qtype=1
    b2.state=DISABLED
    b1.state=NORMAL
    mframe.pack_forget()
    iframe.pack()

def savefunc():
    q=''
    if(qtype==1):
        q=iframe.e1.get()
    else:
        q=mframe.e1.get()
    print(qtype,"saved",q)
    
b1=Button(root,text="mcq",width=20,command=mcqframe)
b2=Button(root,text="intans",width=20,command=intframe)
save=Button(root,text="save",width=20,command=savefunc)
b1.pack()
b2.pack()
save.pack()
mcqf()
intf()
mcqframe()
mframe.pack()


root.mainloop()

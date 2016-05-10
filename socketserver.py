import socket

class databasehelper(object):
    def __init__(self):
        import sqlite3
        sqlite3.connect('onlineexam.db')
    def store(self,uname,password,name):
        print("data stored",uname,password,name)
        

def handlecon(con,z):
    print(con)
    s=con.recv(1024)
    z.store(s,"123","raushan")
    a=con.send("successful".encode())
    print("data send",a)
    con.close()



sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',6969))
sock.listen(5)
z=databasehelper()
while(True):
    print("waiting for connection")
    con,address=sock.accept()
    handlecon(con,z)


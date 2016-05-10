import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ("sending data")
s.connect(("192.168.0.101",6969))
s.send("exit")
input()
s.close()

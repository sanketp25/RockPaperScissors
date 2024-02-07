import socket
from _thread import *

serverAddress = "10.0.0.114"
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((serverAddress,port))
except socket.error as e:
    print(e)

def threaded_client(conn):
    conn.send(str.encode("Connected!"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()
            reply = data
            if not data:
                print("Disconnected!")
                break
            print("Received: ",data)
            print("Sending: ",reply)
            #conn.sendall(str.encode("Connected....."))
        except socket.error as e:
            print(e)
    print("Lost Connection")   
    conn.close()     

s.listen(2)
while True:
    conn,addr = s.accept()
    print("Connected to: ",addr)    
    start_new_thread(threaded_client,(conn,))    
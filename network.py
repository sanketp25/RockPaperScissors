import socket
import pickle

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.port = 5556
        self.serverAddress = "10.0.0.114"
        self.address = (self.serverAddress, self.port) 
        self.p= self.connect()
        print("Value of p is: ",self.p)

    def get_P(self):
        return self.p    
        
    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(4096*4).decode()
        except socket.error as e:
            print(e)
    def send(self,data):
        try:
            print("Data is: ",str.encode(data))
            self.client.send(str.encode(data))   
            return pickle.loads(self.client.recv(4096*4))  
        except socket.error as e:
            print(e) 
    

# print(n.send("Hello"))



# print(n.send("World!"))
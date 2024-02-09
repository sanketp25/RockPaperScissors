import socket
import pickle

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.port = 5557
        self.serverAddress = "10.0.0.114"
        self.address = (self.serverAddress, self.port) 
        self.p= self.connect()

    def get_P(self):
        return self.p    
        
    def connect(self):
        try:
            self.client.connect((self.address))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
    def send(self,data):
        try:
            self.client.send(str.encode(data))   
            return pickle.loads(self.client.recv(2048*2))  
        except socket.error as e:
            print(e) 
    

# print(n.send("Hello"))
# print(n.send("World!"))
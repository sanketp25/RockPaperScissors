import socket
from _thread import *
import pickle
from game import Game



serverAddress = "10.0.0.114"
port = 5556

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((serverAddress,port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection...")

connected = set()
games = {}
idCount = 0



def threaded_client(conn,p,gameId):
    
    global idCount
    print("In threaded....")
    conn.send(str.encode(str(p)))
    reply = ""
    while True:
        try:
            
            response = conn.recv(4096*4)
            data = response.decode()
            # received_data = data
            # print("Received: ",received_data)
            print("While loop in threaded: ",data)
            if gameId in games:
                print("In if, Value of data: ",data)
                game = games[gameId]
                print("Value of response: ",response.decode())
                if not data:
                    print("No Data!")
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p,data)
                    conn.sendall(pickle.dumps(game))    
            else:
                break        

            
        except socket.error as e:
            print(e)
    print("Lost Connection") 
    try:
        del games[gameId]
        print("Closing the game with id: ",gameId)
    except:
        pass
    idCount-=1      
    conn.close()     


while True:
    conn,addr = s.accept()
    #print("Conn is: ",conn)
    print("Connected to: ",addr)    
    idCount+=1
    p = 0
    gameId = (idCount-1)//2
    if idCount % 2:
        games[gameId] = Game(gameId)
        print("Creating new game...")
    else:
        games[gameId].ready = True
        p = 1    
    start_new_thread(threaded_client, (conn, p, gameId))  
import socket
import threading

# Port No. (Free port no)
PORT = 5050
# ip addres of the current pc (This is my Local ip)
HOST = "192.168.0.108" #socket.gethostbyname(socket.getfqdn(socket.gethostname()))
# binding Variable
ADDR = (HOST, PORT)
# content storing capacity (byts)
capasity = bytes
# message type
formate = "utf-8"
# connection type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind ip address and port
server.bind(ADDR)
server.listen(5)
print("Server is Started")

clientsocket, address = server.accept()
print(f"Connection from {address} has been established!")
def send():
    while True:
        x = input()
        clientsocket.send(capasity(x, formate))

def recive():
    while True:
        a = clientsocket.recv(int(1024)).decode(formate)
        print(f"[{address}] {a}")


thread1 = threading.Thread(target=send)
thread2 = threading.Thread(target=recive)
thread1.start()
thread2.start()

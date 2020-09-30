import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
capacity = bytes
SERVER = "192.168.0.108" #socket.gethostbyname(socket.getfqdn(socket.gethostname()))
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def recive():
    while True:
        msg = client.recv(1024).decode(FORMAT)
        print(f"[Server] {msg}")

def send():
    while True:
        c = input()
        client.send(capacity(c, FORMAT))

thread1 = threading.Thread(target=send)
thread2 = threading.Thread(target=recive)
thread1.start()
thread2.start()
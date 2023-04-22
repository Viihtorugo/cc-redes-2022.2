#!/usr/bin/python3 

import socket

HEADER = 2048
PORT = 12000
FORMAT = 'utf-8'
SERVER = "192.168.0.11"
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)
print(ADDR)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))

while True:
    msg = input("Digite !DISCONNECT para finalizar thread: ")
    if msg == DISCONNECT_MESSAGE:
        break
    
    send(msg)
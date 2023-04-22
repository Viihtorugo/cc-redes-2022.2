#!/usr/bin/python3 

import socket

HEADER = 2048
PORT = 12000
FORMAT = 'utf-8'
SERVER = "192.168.0.11"
ADDR = (SERVER, PORT)
print(ADDR)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
#!/usr/bin/python3 

import socket
import threading

HEADER = 2048
PORT = 12000
SERVER = ""
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr} {msg}]")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
    


def start():
    server.listen()
    print(f"[SERVIDOR CONECTADO] Servidor está conectado {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ATIVANDO CONECÇÕES] {threading.active_count() - 1}")
        


print("[STARTING] servidor esta iniciando...")
start()
print("[ENDING] servidor esta finalizando...")
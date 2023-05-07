#!/usr/bin/python3 

import socket
import threading

HEADER = 2048
PORT = 12000
SERVER = ""
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!EXIT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def fat (num):
    if num <= 0: 
        return 1
    
    return num * fat (num - 1)

def get(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        return conn.recv(msg_length).decode(FORMAT)
    else:
        return DISCONNECT_MESSAGE

def send(conn, msg):
    try:
        conn.send(msg.encode(FORMAT))
    except:
        print("Não existe mais conexão!")
        return


def handle_client(conn, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")

    connected = True
    while connected:
        msg = get(conn)
        print(f"[{addr} {msg}]")
        if msg.lower() == "fatorial":
            send(conn, "Digite um número: ")
            msg = get(conn)
            print(f"[{addr} fatorial:{msg}]")
            try:
                msg = int(msg)
                if (msg >= 0):
                    send(conn, f"Fatorial de {msg} é igual {fat(msg)}")
                else:
                    send(conn, f"Digite um número maior que ou igual a 0")
            except:
                send(conn, "Você não digitou um número!");
        elif msg == DISCONNECT_MESSAGE:
            connected = False
            print(f"[DESCONECTANDO] {addr}")
            send(conn, "Desconectando...");
            conn.close()
            return
        else:
            conn.send("Você está conectado no servidor!".encode(FORMAT))
        

def start():
    server.listen()
    print(f"[SERVIDOR CONECTADO] Servidor está conectado {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[THREADS ATIVAS] {threading.active_count() - 1}")

print("[STARTING] servidor esta iniciando...")
start()
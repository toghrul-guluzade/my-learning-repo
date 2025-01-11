import threading
import socket

host = '192.168.1.69'
port = 12345

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((host, port))
server.listen()
print(f"Server is listening on {host}:{port}")

clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f"{alias} has left the chat room!".encode('utf-8'))
            aliases.remove(alias)
            break
        

def receive():
    while True:
        print("Server is running and listening for connections")
        client, address = server.accept()
        print(f"Connection is established with {str(address)}")
        client.send('alias'.encode('utf-8'))
        alias = client.recv(1024)
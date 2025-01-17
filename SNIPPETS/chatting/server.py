from cryptography.fernet import Fernet
import csv
import os
import authentication as auth
import socket

#s = socket.socket()
#port = 12345
#s.connect(('192.168.1.69', port))
#print(s.recv(1024))
#s.close()

def authentication(client_socket):
  client_socket.send(b"Do you want to sign up(0) or sign in?(1): ")
  condition = client_socket.recv(1024).decode()

  if condition == "0":
    client_socket.send(b"Enter username for sign up: ")
    username = client_socket.recv(1024).decode()
    client_socket.send(b"Enter password: ")
    password = client_socket.recv(1024).decode()
    auth.userSignUp(username, password)
    client_socket.send(b"User signed up successfully")
  elif condition == "1":
    client_socket.send(b"Enter username for sign in: ")
    username = client_socket.recv(1024).decode()
    client_socket.send(b"Enter password: ")
    password = client_socket.recv(1024).decode()
    if auth.userSignIn(username, password):
      client_socket.send(b"User signed in")
    else: 
      client_socket.send(b"Invalid credentials")
  else:
    client_socket.send(b"Invalid input. Disconnecting...")
    client_socket.close()
    
if __name__ == "__main__":
  
  server_socket = socket.socket()
  port = 12345
  server_socket.bind(('192.168.1.68', port))
  server_socket.listen(5)
  print("Server is up and running")

  while True:
    client_socket, client_address = server_socket.accept()
    print("Connection from: ", client_address)
    client_socket.send(b"Welcome to the server")
    #Receive Message from client
    message = client_socket.recv(1024).decode()
    print("Client: ", message)

    if message == "auth":
      authentication(client_socket)
    else: 
      client_socket.send(b"Invalid input. Disconnecting...")
      client_socket.close()

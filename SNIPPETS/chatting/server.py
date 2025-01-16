import socket
from cryptography.fernet import Fernet
import csv
import os

if not os.path.exists("chatting//key.txt"):
  key = Fernet.generate_key()
  with open("chatting//key.txt", "wb") as file:
    file.write(key)

  with open("chatting//key.txt", "rb") as file:
    key = file.read()
else:
  with open("chatting//key.txt", "rb") as file:
    key = file.read()

def userSignUp ():
  username = input("Enter your username: ")
  password = Fernet(key).encrypt(input("Enter your password: ").encode())
  with open ("chatting//users.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["username", "password"])
    if file.tell() == 0: writer.writeheader()
    writer.writerow({"username": username, "password": password.decode()})


def userSignIn():
  username = input("Enter your username: ")
  password = input("Enter your password: ").encode()
  with open ("chatting//users.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      if row["username"] == username:
        print(row["password"])
        print(row["password"].encode())
        stored_password = Fernet(key).decrypt(row["password"].encode())
        #print(Fernet(key).decrypt(password))   #I can get a correct output here
       # print(Fernet(key).decrypt(stored_password))   #it gives me an error here
       # print(password)
      if stored_password == password:
        print("Welcome, ", username)
        break


    

#s = socket.socket()
#port = 12345
#s.connect(('192.168.1.69', port))
#print(s.recv(1024))
#s.close()

if __name__ == "__main__":
  condition = input("Do you want to sign up(0) or sign in?(1): ")
  if condition == "0":
    userSignUp()
  elif condition == "1":    
    userSignIn()
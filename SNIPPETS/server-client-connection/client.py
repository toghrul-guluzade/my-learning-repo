import socket

s = socket.socket()
port = 12345
s.connect(('192.168.1.69', port))
print(s.recv(1024))
s.close()
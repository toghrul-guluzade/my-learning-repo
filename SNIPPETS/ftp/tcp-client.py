import socket

if  __name__ == "__main__":
    host = '192.168.1.69'
    port = 8080
    totalClients = int(input("Enter the number of clients you want to connect: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(totalClients)
    print(f"Server is listening on {host}:{port}")

    conections = []
    print("Waiting for connections...")

    for i in range(totalClients):
        conn, addr = sock.accept()
        print(f"Connection established with {addr}")
        conections.append(conn)

    fileno = 0
    idx = 0 

    data 
        
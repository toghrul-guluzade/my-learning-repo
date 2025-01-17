import socket

def main():
  client_socket = socket.socket()

  server_ip = '192.168.1.68'
  port = 53147


  try: 

    client_socket.settimeout(5)
    client_socket.connect((server_ip, port))
    print("Connected to server at: ", server_ip, port)

    while True:
      server_message = client_socket.recv(1024).decode()
      print("Server: ", server_message)
      if "Disconnecting" in server_message:
        print("Server closed the connection")
        break
      
      user_input = input("Enter message to server: ")
      client_socket.send(user_input.encode())

  except ConnectionRefusedError:
    print("Server is not up and running")

  except TimeoutError:
    print("Connection timed out. Server is not responding")

  except Exception as e:
    print("An error occurred: ", e)
  

  finally:
    client_socket.close()

if __name__ == "__main__":
  main()




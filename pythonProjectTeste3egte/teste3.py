import socket

def startclient():
    serverip = '170.254.163.90'  # Public IP address of the server
    serverport = 12345           # Port number used by the server

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((serverip, serverport))

    try:
        while True:
            message = input("Enter message to send: ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024).decode()
            print(f"Received from server: {data}")
    except KeyboardInterrupt:
        print("Client interrupted.")
    finally:
        client_socket.close()

startclient()
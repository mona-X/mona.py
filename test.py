import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 4444))

data = ""
with open("text.txt", 'rb') as file:
    data = file.read()

sock.sendall(data)

sock.close()

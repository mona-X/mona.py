import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("0.0.0.0", 4444))
sock.listen(5)
client, addr = sock.accept()

f = open('recv.txt', 'wb')

while True:
    dummy = ""
    dummy = client.recv(1024)
    if not dummy:
        print("transfer complete!")
        break
    f.write(dummy)
    dummy = ""


sock.close()

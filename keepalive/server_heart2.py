import socket

server = socket.socket()

server.bind(('localhost', 9999))
server.listen(5)

print("server start....")

while True:
    client, addr = server.accept()
    print('peer address: ', addr)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    client.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 60)
    client.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 3)
    client.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 20)

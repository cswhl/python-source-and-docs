from socket import *

ADDR = ('localhost', 21568)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    data = input('> ')
    if not data:
        break
    c = tcpCliSock.send(f'{data}\r\n'.encode())
    print(f'c={c}')
    data = tcpCliSock.recv(1024)
    print(f'data={data}')
    if not data:
        break
    print(data.strip())

tcpCliSock.close()

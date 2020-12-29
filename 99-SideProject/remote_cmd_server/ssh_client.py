import struct
from socket import *

ADDR = ('localhost', 21569)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    cmd = input('> ')
    if not cmd:
        break
    tcpCliSock.send(f'{cmd}'.encode())

    data, recv_num = '', 0
    length = struct.unpack('i', tcpCliSock.recv(4))[0]
    while recv_num < length:
        mes = tcpCliSock.recv(1024).decode('utf8')
        recv_num += len(mes)
        data += mes

    print(f'{data}')

tcpCliSock.close()

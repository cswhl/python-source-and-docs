#!/usr/bin/python3

import struct
import json
from socket import *

ADDR = ('localhost', 21569)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    cmd = input('> ')
    if not cmd:
        break
    tcpCliSock.send(f'{cmd}'.encode()) # noqa

    data, recv_num = '', 0

    # 1. 接收固定长度的报头
    header_length = struct.unpack('i', tcpCliSock.recv(4))[0]
    # print(f'header_length={header_length}')
    # 2. 接收报头,并解码、JSON反序列化得到dict
    header_json = tcpCliSock.recv(header_length).decode('utf8')
    header = json.loads(header_json)
    # print(f'header={header}')
    length = header['total_size']
    while recv_num < length:
        mes = tcpCliSock.recv(1024).decode('utf8')
        recv_num += len(mes)
        data += mes

    print(f'{data}')

tcpCliSock.close()

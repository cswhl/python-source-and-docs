#!/usr/bin/python3

import os
import socket
import struct
from socketserver import BaseRequestHandler, ThreadingTCPServer
from time import time, sleep

ADDR = '', 21569


class ThreadTCPRequestHandler(BaseRequestHandler):
    timeout = 3600

    def setup(self):
        self.request.settimeout(self.timeout)
        print(f'{self.client_address} 连接到服务器...')

    def handle(self):
        while True:
            try:
                cmd = self.request.recv(1024).decode('utf8')
            except socket.timeout:
                print(f'{self.client_address} 接收超时，即将断开连接...')
                break

            if not cmd:
                break

            print(f'执行cmd: {cmd}')
            with os.popen(cmd=cmd) as fobj:
                data = fobj.read()
                if not data:
                    data = "命令错误，请重新输入"
                data = cmd + ':\r\n' + data
                print(f'data2={data}')
                header = struct.pack('i', len(data))
                self.request.send(header)
                self.request.sendall(f'{data}'.encode('utf8')) # 数据

    def finish(self):
        print(f'{self.client_address} 断开连接...')


ThreadingTCPServer.allow_reuse_address = True

with ThreadingTCPServer(ADDR, ThreadTCPRequestHandler) as tcpServ:
    print('waiting for connection')
    tcpServ.serve_forever()

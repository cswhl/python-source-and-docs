#!/usr/bin/python3

from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

ADDR = 'localhost', 21567

class MyRequestHandler(SRH):
    '''创建请求类，处理客户请求'''

    def handle(self):
        # 请求处理
        print(f'...connected from:{self.client_address}')
        self.wfile.write(f'[{ctime()}] {self.rfile.readline()}'.encode('utf8') )

with TCP(ADDR, MyRequestHandler) as tcpServ:
    print('waiting for connection')
    tcpServ.serve_forever() # 运行服务器，直到shutdown()

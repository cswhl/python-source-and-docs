#!/usr/bin/python3

from socketserver import StreamRequestHandler as SRH
from socketserver import ThreadingTCPServer
from time import ctime
import threading

ADDR = 'localhost', 21568

class MyRequestHandler(SRH):
    '''创建请求类，处理客户请求'''

    def handle(self):
        # 请求处理
        print(threading.current_thread())
        print(f'...connected from:{self.client_address}')
        print(self.request)
        self.wfile.write(f'[{ctime()}] {self.rfile.readline()}'.encode('utf8') )

with ThreadingTCPServer(ADDR, MyRequestHandler) as tcpServ:
    print('waiting for connection')
    print(threading.current_thread())
    tcpServ.serve_forever() # 运行服务器，直到shutdown()

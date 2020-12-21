#!/usr/bin/python3

from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime
import threading

ADDR = 'localhost', 21568

class MyRequestHandler(SRH):
    '''创建请求类，处理客户请求'''

    def handle(self):
        # 请求处理
        print(f'...connected from:{self.client_address}')
        print(self.request)
        print(threading.current_thread()) # 一直使用主线程，即没有开启新的线程
        self.wfile.write(f'[{ctime()}] {self.rfile.readline()}'.encode('utf8') )

with TCP(ADDR, MyRequestHandler) as tcpServ:
    tcpServ.fileno()
    print('waiting for connection')
    tcpServ.serve_forever() # 运行服务器，直到shutdown()

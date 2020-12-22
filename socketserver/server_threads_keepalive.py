#!/usr/bin/python3

from socketserver import StreamRequestHandler as SRH, TCPServer as TCP
from socketserver import ThreadingTCPServer
from time import ctime
import threading

ADDR = 'localhost', 21568

class MyRequestHandler(SRH):
    '''创建请求类，处理客户请求'''

    def handle(self):
        while True: # 长连接
            # 请求处理
            print(f'...connected from:{self.client_address}')
            data = self.rfile.readline()
            if not data: break
            self.wfile.write(f'[{ctime()}] {data}'.encode('utf8') )

ThreadingTCPServer.allow_reuse_address = True # 允许地址复用
with ThreadingTCPServer(ADDR, MyRequestHandler) as tcpServ:
    print('waiting for connection')
    # print(threading.current_thread())
    tcpServ.serve_forever() # 运行服务器，直到shutdown()

#!/usr/bin/python3

from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer
import socket
from time import ctime
import threading

ADDR = 'localhost', 21568

client_addr = []
client_socket = []


class ThreadedTCPRequestHandler(BaseRequestHandler):
    '''继承超类，实现自定义setup、handle、finish方法
    允许地址复用、长连接、超时断开
    如果是继承StreamRequestHandler子类则无法自定义setup、finish方法'''

    ip = ""
    port = 0
    timeOut = 6     # 设置超时时间变量

    def setup(self):
        self.ip = self.client_address[0].strip()     # 获取客户端的ip
        self.port = self.client_address[1]           # 获取客户端的port
        self.request.settimeout(self.timeOut)        # 对socket设置超时时间
        print(self.ip + ":" + str(self.port) + "连接到服务器！")
        client_addr.append(self.client_address)  # 保存到队列中
        client_socket.append(self.request)      # 保存套接字socket

    def handle(self):
        while True:  # while循环
            try:
                data = str(self.request.recv(1024), 'utf8')
            except socket.timeout:  # 如果接收超时会抛出socket.timeout异常
                print(self.ip + ":" + str(self.port) + "接收超时！即将断开连接！")
                break       # 记得跳出while循环

            if data:    # 判断是否接收到数据
                cur_thread = threading.current_thread()
                response = bytes(
                    "{}: {}".format(
                        cur_thread.name,
                        data),
                    'ascii')
                self.request.sendall(response)

    def finish(self):
        print(self.ip + ":" + str(self.port) + "断开连接！")
        client_addr.remove(self.client_address)
        client_socket.remove(self.request)


ThreadingTCPServer.allow_reuse_address = True # 允许地址复用

with ThreadingTCPServer(ADDR, ThreadedTCPRequestHandler) as tcpServ:
    print('waiting for connection')
    # print(threading.current_thread())
    tcpServ.serve_forever()  # 运行服务器，直到shutdown()

from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer
import socket
from time import ctime
import threading
import re

ADDR = 'localhost', 21568

client_addr = []
client_socket = []


class HttpConst(object):
    '''常量类'''

    CRLF = '\r\n'
    CR = 13
    LF = 10
    # keep space, for split
    GET = 'GET '
    POST = 'POST '
    HOST = 'Host: '

class 

class ThreadedTCPRequestHandler(BaseRequestHandler):
    '''继承超类，实现自定义setup、handle、finish方法
    允许地址复用、长连接、超时断开
    如果是继承StreamRequestHandler子类则无法自定义setup、finish方法'''

    ip = ""
    port = 0
    timeOut = 3     # 设置超时时间变量

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
                request_data = self.request.recv(1024).decode('utf8')
            except socket.timeout:  # 如果接收超时会抛出socket.timeout异常
                print(self.ip + ":" + str(self.port) + "接收超时！即将断开连接！")
                break       # 记得跳出while循环

            if request_data:    # 判断是否接收到数据
                request_data_lines = request_data.splitlines()
                print(request_data_lines)
                # 1. get file_name
                file_name = ""
                ret = re.match(r"[^/]+(/[^ ]*)", request_data_lines[0])
                if ret:
                    file_name = '/index.html' if ret.group(
                        1) == '/' else ret.group(1)

                print(f"file_name={file_name}")

                # 2. deal response, and return
                try:
                    with open('./html' + file_name, 'rb') as f:
                        html_content = f.read()
                except Exception:
                    response_header = "HTTP/1.1 404 NOT FOUND"
                    html_content = 'file not found'.encode('utf8')
                else:
                    response_header = "HTTP/1.1 200 OK"

                response = f'{response_header}' + HttpConst.CRLF
                response += HttpConst.CRLF

                self.request.send(response.encode('utf8'))
                self.request.send(html_content)

    def finish(self):
        print(self.ip + ":" + str(self.port) + "断开连接！")
        client_addr.remove(self.client_address)
        client_socket.remove(self.request)


if __name__ == '__main__':
    ThreadingTCPServer.allow_reuse_address = True  # 允许地址复用
    with ThreadingTCPServer(ADDR, ThreadedTCPRequestHandler) as wsgi_server:
        print('waiting for connection')
        wsgi_server.serve_forever()  # 运行服务器，直到shutdown()

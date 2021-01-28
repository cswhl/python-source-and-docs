from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer
import socket
from time import ctime
import threading
import re
import os
import sys
import mini_frame

ADDR = '0.0.0.0', int(sys.argv[1])
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


class HttpHandler(object):
    def __init__(self, request_data):
        self.request_data = request_data

    def _get_file_name(self):
        # 1. get file_name
        request_data_lines = self.request_data.splitlines()
        print(request_data_lines)
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_data_lines[0])
        if ret:
            file_name = '/index.html' if ret.group(
                1) == '/' else ret.group(1)

        print(f"file_name={file_name}")
        return file_name

    def get_response(self):
        # deal response, and return

        # 1. find static source
        file_name = self._get_file_name()
        if not file_name.endswith(".py"):
            try:
                with open('./html' + self._get_file_name(), 'rb') as f:
                    response_body = f.read()
            except Exception:
                response_line = "HTTP/1.1 404 NOT FOUND"
                response_body = 'file not found'.encode('utf8')
            else:
                response_line = "HTTP/1.1 200 OK"

        # 2. find dynamic
        else:
            response_line = "HTTP/1.1 200 OK"

            # 2.1 set env
            env = dict()
            env['path_info'] = file_name
            # 2.2 set start_response
            response_body = mini_frame.application(env, self._set_response_header).encode('utf8')

        response = f'{response_line}' + HttpConst.CRLF
        response += HttpConst.CRLF
        response = response.encode('utf8')

        return (response, response_body)

    def _set_response_header(self, status, headers):
        self.satus = status
        # elem tuple：(name, value)?
        self.headers = []


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
                http_handler = HttpHandler(request_data)
                response, response_body = http_handler.get_response()
                self.request.send(response)
                self.request.send(response_body)
            break

    def finish(self):
        print(self.ip + ":" + str(self.port) + "断开连接！")
        client_addr.remove(self.client_address)
        client_socket.remove(self.request)


if __name__ == '__main__':
    ThreadingTCPServer.allow_reuse_address = True  # 允许地址复用
    with ThreadingTCPServer(ADDR, ThreadedTCPRequestHandler) as wsgi_server:
        print('waiting for connection')
        wsgi_server.serve_forever()  # 运行服务器，直到shutdown()

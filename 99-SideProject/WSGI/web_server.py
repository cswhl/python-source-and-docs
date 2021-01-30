from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer
import socket
from time import ctime
import re
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

    def _set_path_info(self):
        # 1. get file_name
        request_data_lines = self.request_data.splitlines()
        print(request_data_lines)
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_data_lines[0])
        if ret:
            file_name = '/index.html' if ret.group(
                1) == '/' else ret.group(1)

        self.file_name = file_name

    def _set_static_source(self):
        self.response_headers = ''
        try:
            with open('./html' + self.file_name, 'rb') as f:
                self.response_body = f.read()
        except Exception:
            self.response_line = "HTTP/1.1 404 NOT FOUND"
            self.response_body = 'file not found'.encode('utf8')
        else:
            self.response_line = "HTTP/1.1 200 OK"

    def _set_dynamic_source(self):
        self.response_headers = ''
        env = dict()
        env['path_info'] = self.file_name
        self.response_body = mini_frame.application(
            env, self.set_response_header).encode('utf8')
        self.response_line = f'HTTP/1.1 {self.status}'
        for header in self.headers:
            self.response_headers += f'{header[0]}: {header[1]}' + HttpConst.CRLF

    def _set_response(self):
        self.response = self.response_line + HttpConst.CRLF
        self.response += self.response_headers + HttpConst.CRLF
        self.response = self.response.encode('utf8') + self.response_body

    def get_response(self):
        self._set_path_info()

        if not self.file_name.endswith(".py"):
            self._set_static_source()
        else:
            self._set_dynamic_source()
        self._set_response()

        return self.response

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [('server', 'web v1.0')] + headers


class ThreadedTCPRequestHandler(BaseRequestHandler):
    ip = ""
    port = 0
    timeOut = 3

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
                response = http_handler.get_response()
                self.request.send(response)
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

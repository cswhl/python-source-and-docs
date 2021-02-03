from socketserver import BaseRequestHandler
from socketserver import ThreadingTCPServer
import socket
from time import ctime
import re
import sys
import mini_frame

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

            if request_data:
                http_handler = HttpHandler(request_data)
                response = http_handler.get_response()
                self.request.send(response)
            break

    def finish(self):
        print(self.ip + ":" + str(self.port) + "断开连接！")
        client_addr.remove(self.client_address)
        client_socket.remove(self.request)


class HttpHandler(object):
    def __init__(self, request_data):
        self.request_data = request_data
        self.file_path = self._get_path_of_file()

    def _get_path_of_file(self):
        request_data_lines = self.request_data.splitlines()
        ret = re.match(r"[^/]+(/[^ ]*)", request_data_lines[0])
        file_path = ""
        if ret:
            file_path = '/index.html' if ret.group(
                1) == '/' else ret.group(1)

        return file_path

    def get_response(self):
        if not self.file_path.endswith(".py"):
            self._set_static_page_info()
        else:
            self._set_dynamic_page_info()
        self._combinate_response_page_info()

        return self.response

    def _combinate_response_page_info(self):
        self.response = self.response_line + HttpConst.CRLF
        self.response += self.response_headers + HttpConst.CRLF
        self.response = self.response.encode('utf8') + self.response_body

    def _set_static_page_info(self):
        self.response_headers = ''
        try:
            with open('./html' + self.file_path, 'rb') as f:
                self.response_body = f.read()
        except Exception:
            self.response_line = "HTTP/1.1 404 NOT FOUND"
            self.response_body = 'file not found'.encode('utf8')
        else:
            self.response_line = "HTTP/1.1 200 OK"

    def _set_dynamic_page_info(self):
        env = dict()
        env['path_info'] = self.file_path
        self.response_body = mini_frame.application( env, self.set_response_header).encode('utf8') # noqa
        self.response_line = f'HTTP/1.1 {self.status}'
        self.response_headers = ''
        for header in self.headers:
            self.response_headers += f'{header[0]}: {header[1]}' + HttpConst.CRLF # noqa

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [('server', 'web v1.0')] + headers


def get_():
    if len(sys.argv) == 3:
        port = sys.argv[1]
        frame_app_name = sys.argv[2]
        print(port, frame_app_name)
    else:
        print("请按以下方式运行:")
        print("python3 xxx.py 9999 mini_frame:application")
        return

    ret = re.match(r'([^:]+):(.*)', frame_app_name)
    if ret:
        frame_name = ret.group(1)
        app_name = ret.group(2)
        print(frame_name, app_name)
    else:
        print("请按以下方式运行:")
        print("python3 xxx.py 9999 mini_frame:application")
        return

    frame = __import__(frame_name)
    app = getattr(frame, app_name)


if __name__ == '__main__':
    ADDR = '0.0.0.0', int(sys.argv[1])
    get_()
    ThreadingTCPServer.allow_reuse_address = True  # 允许地址复用
    with ThreadingTCPServer(ADDR, ThreadedTCPRequestHandler) as wsgi_server:
        print('waiting for connection')
        wsgi_server.serve_forever()  # 运行服务器，直到shutdown()

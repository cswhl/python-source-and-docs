#!/usr/bin/python3

import socket
from urllib.parse import urlparse


class Client(object):
    '''使用socket模拟http请求，socket非阻塞模式
    非阻塞模式下，需不断轮询发起I/O请求，请求失败则内核返回错误码，成功则返回复制的数据
    '''

    def __init__(self, url):
        url = urlparse(url)
        self.host, self.path = url.netloc, [url.path, '/'][url.path == '']
        self.socket = socket.socket()
        self.socket.setblocking(False)
        try:
            self.socket.connect((self.host, 80))
        except BlockingIOError as ret:
            print(f'connect {ret}')  # noqa

    def send_request(self):
        while True:
            try:
                self.socket.send(
                    "GET {} HTTP/1.1\r\nHost: {}\r\nConnection:close\r\n\r\n".format(
                        self.path, self.host).encode('utf-8'))
                break
            except socket.error as ret:
                print(f'send {ret}')  # noqa
                pass

    def recv_response(self):
        self.data = b''
        while True:
            try:
                rev = self.socket.recv(1024)
                if rev == b'':
                    break
                self.data += rev
            except socket.error as ret:
                print(f'recv {ret}')  # noqa
                pass

    def run(self):
        self.send_request()
        self.recv_response()
        html_body = self.data.split(b'\r\n\r\n')[1]
        return html_body

    def close(self):
        self.socket.close()


if __name__ == '__main__':
    client = Client("http://www.baidu.com")
    data = client.run()
    client.close()
    print(data.decode('utf-8'))

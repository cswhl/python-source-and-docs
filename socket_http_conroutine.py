#!/usr/bin/python3

import socket
from urllib.parse import urlparse
# DefaultSelector默认选择器，使用当前平台上可用的最高效的实现(select/poll/epoll)
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


class Client(object):
    '''select + callback + eventLoop：单线程并发
    只处理准备好socket事件，无需等待I/O;省去了线程切换的开销'''

    def __init__(self, url):
        url = urlparse(url)
        self.host, self.path = url.netloc, [url.path, '/'][url.path == '']
        self.socket = socket.socket()
        self.socket.connect((self.host, 80))

    def send_request(self):
        self.socket.send(
            "GET {} HTTP/1.1\r\nHost: {}\r\nConnection:close\r\n\r\n".format(
                self.path, self.host).encode('utf-8'))

    def recv_response(self):
        self.data = b''
        while True:
            rev = self.socket.recv(1024)
            if rev == b'':
                break
            self.data += rev

    def run(self):
        self.send_request()
        self.recv_response()
        html_body = self.data.split(b'\r\n\r\n')[1]
        return html_body

    def close(self):
        self.scoket.close()


if __name__ == '__main__':
    client = Client("http://www.baidu.com")
    data = client.run()
    print(data.decode('utf-8'))

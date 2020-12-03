#!/usr/bin/python3

import socket
from urllib.parse import urlparse


class Client(object):
    '''使用socket模拟http请求，socket阻塞模式'''
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

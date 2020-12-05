#!/usr/bin/python3

import socket
from urllib.parse import urlparse
# DefaultSelector默认选择器，使用当前平台上可用的最高效的实现(select/poll/epoll)
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


class Client(object):
    '''负责连接、 发送和接受'''
    def __init__(self, url):
        url = urlparse(url)
        self.host, self.path = url.netloc, [url.path, '/'][url.path == '']
        self.sock = socket.socket()
        self.sock.setblocking(False)
        self.data = b''
        try:
            self.sock.connect((self.host, 80))
        except BlockingIOError as ret:  # noqa
            pass

    def send_request(self):
        self.sock.send(
            "GET {} HTTP/1.1\r\nHost: {}\r\nConnection:close\r\n\r\n".format(
                self.path, self.host).encode('utf-8'))

    def recv_response(self):
        rev = self.sock.recv(1024)
        if rev:
            self.data += rev
            return True
        return False

    def end(self):
        html_body = self.data.split(b'\r\n\r\n')[1]
        self.sock.close()
        print(html_body)
        print('\n')
        return html_body


'''select + callback + eventLoop：单线程并发
只处理准备好socket事件，无需等待I/O;省去了线程切换的开销
回调模式:底层调用高层'''


class Select(object):
    '''创建selector,负责注册和取消注册socket读写事件、'''

    def __init__(self):
        self.selector = DefaultSelector()
        self.clients = {}

    def startListening(self, client):
        # add client,monitor socked wtite event
        self.clients[client.sock] = client
        # 注册socket写事件
        self.selector.register(client.sock, EVENT_WRITE, self.connected)

    def connected(self, key):
        # connect host,and monitor socket read event
        self.selector.unregister(key.fileobj)
        sock = key.fileobj
        self.clients[sock].send_request()
        self.selector.register(sock, EVENT_READ, self.do_read)

    def do_read(self, key):
        # read data ,if data is empty, then unregister socket and end
        sock = key.fileobj
        client = self.clients[sock]
        if client.recv_response():
            return
        self.selector.unregister(sock)
        client.end()


def event_loop():
    while True:
        events = sel.selector.select()
        for key, mask in events:
            print(key, mask)
            callback = key.data
            callback(key)


if __name__ == '__main__':
    urls = ['http://www.baidu.com', 'http://httpbin.org/']
    sel = Select()
    for url in urls:
        sel.startListening(Client(url))
    event_loop()
    sel.selector.close()

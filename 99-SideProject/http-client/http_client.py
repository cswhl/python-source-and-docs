#!/usr/bin/python3


import sys
import re
import socket
import ssl
import unittest
from urllib.parse import urlparse
from http.client import HTTP_PORT, HTTPS_PORT
from urllib.error import URLError
from abc import ABC, abstractmethod


class RecvErr(Exception):
    pass


class HttpConst(object):
    '''常量类'''

    CRLF = '\r\n'
    CR = 13
    LF = 10
    # keep space, for split
    GET = 'GET '
    POST = 'POST '
    HOST = 'Host: '


def validate_url(argv):
    '''判断url是否合法'''

    if len(argv) != 2:
        print(sys.stderr, 'URL Required')
        sys.exit(-1)

    url = argv[1]
    if not re.match(r'^https?:/{2}\w.+$', url.strip()):
        print('url地址不合法')
        raise URLError('URL is unavailable')
    return True


class HttpURL(object):
    '''构造url对象'''

    def __init__(self, url):
        self._url = urlparse(url.strip())

    @property
    def protocol(self):
        return self._url.scheme

    @property
    def host(self):
        return self._url.hostname

    @property
    def path(self):
        return self._url.path if self._url.path else '/'

    @property
    def port(self):
        return self._url.port if self._url.port else self._default_port(self.protocol)  # noqa

    def _default_port(self, protocol):
        return HTTP_PORT if self.protocol == 'http' else HTTPS_PORT

    @property
    def request_packet(self):  # noqa
        '''拼接http请求'''

        request = ''
        # constructor rquest line
        request += HttpConst.GET + self.path + ' ' + 'HTTP/1.1'
        request += HttpConst.CRLF
        # header
        request += HttpConst.HOST + self.host
        request += HttpConst.CRLF
        request += 'Connection: close'
        request += HttpConst.CRLF
        # space line
        request += HttpConst.CRLF
        # body

        return request


class HttpClient(object):
    '''客户端'''

    def __init__(self, url: HttpURL):
        self.sock = socket.socket() if url.protocol == 'http' else ssl.wrap_socket(socket.socket())  # noqa
        self.sock.settimeout(3)
        try:
            addresses = url.host, url.port
            self.sock.connect(addresses)
        except socket.error as ret:
            print(f'web服务器地址错误{ret}')
            sys.exit(-1)
        self.url = url

    def __send(self, Request):
        '''发送请求'''
        request = Request(self.sock, self.url.request_packet)
        request.send_request()

    def __recv(self, Response):
        '''接受响应'''
        try:
            self.response = Response(self.sock)
            self.response.get_all()
            print('\n')
            print(self.response.head)
            # print(self.response.body)
        except RecvErr as res:
            print(f'client.recv错误--{res}')

    def run(self, Request, Response):
        self.__send(Request)
        self.__recv(Response)

    def stop(self):
        self.sock.close()


class Request(ABC):
    @abstractmethod
    def send_request(self):
        pass


class HttpRequest(Request):
    '''报文请求'''

    def __init__(self, sock, http_request: str):
        self.sock = sock
        self.http_request = http_request

    def send_request(self):
        self.sock.send(self.http_request.encode('utf-8'))


class Response(ABC):
    @abstractmethod
    def get_all(self):
        pass


class HttpResponse(Response):
    '''处理响应的报文'''

    def __init__(self, sock):
        self.sock = sock
        rev = b''
        # 获取响应报文的首帧数据
        while b'\r\n\r\n' not in rev:
            rev += self.sock.recv(1024)  # .decode('utf-8')

        try:
            # [:2]防止响应报文含不只一个'\r\n\r\n'
            self.head, self.body = rev.split(b'\r\n\r\n')[:2]
            self.head = self.head.decode('utf-8')
            self.header_lines = self.head.split('\r\n')
        except socket.error as res:
            print(f'报文响应接受数据错误:{res}')
            raise RecvErr('接受数据错误')
        except BaseException as res:
            print(f'报文响应实例初始化时错误:{res}')
            raise RecvErr('接受数据错误')

    def get_all(self):
        self.get_line()
        self.get_header_map()
        self.get_body()

    def get_line(self):
        # 获取响应行
        self.request_line = self.header_lines[0]

    def get_header_map(self):
        # 获取响应头对应的map
        header_map = {}
        for header in self.header_lines[1:]:
            print(header)
            header_map.update([header.split(': ')])
        self.header_map = header_map

    def get_body(self):
        # 获取响应体
        try:
            if self.header_map['Transfer-Encoding'] == 'chunked':
                self._read_chunked()
        except KeyError as ret:
            self._read_content_length()
            print(f'fun get_body error={ret}')
        # 如果是gzip格式，则需要在此出解压缩
        # ...

    def _read_content_length(self):
        # 获取content-Length响应体
        self._read_content()

    def _read_chunked(self):
        # 获取分块编码形式的响应体
        self._read_content()
        # chunked解码
        # ...

    def _read_content(self):
        try:
            rev = self.sock.recv(1024)  # .decode('utf-8')
            while rev:
                self.body += rev
                rev = self.sock.recv(1024)  # .decode('utf-8')
        except socket.timeout as res:
            print(f'sock.recv接受数据超时---"Error:{res}"')  # noqa


def main():
    if not validate_url(sys.argv):
        return

    url = HttpURL(sys.argv[-1])
    client = HttpClient(url)
    client.run(HttpRequest, HttpResponse)
    try:
        url = HttpURL(client.response.header_map['Location'])
        try:
            if client.response.header_map['Connection'] == 'close':
                # 服务器断开连接，则关闭客户端后重开一个客户端
                client.stop()
                client = HttpClient(url)
            client.run(HttpRequest, HttpResponse)
        except KeyError as ret:
            print(ret)
    except KeyError as ret:
        print(f'ret={ret}')


class TestUrl(unittest.TestCase):
    '''测试用例'''
    url = 'https://httpbin.org/'
    result = 'GET / HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n'

    def test_validate_url(self):
        '''1 测试validate_url函数'''
        self.assertTrue(validate_url(['', self.url]))
        self.assertRaises(URLError, validate_url, ['', '://docs.pyhton/'])
        self.assertRaises(SystemExit, validate_url, [''])

    def test_HttpURL(self):
        '''2 测试URL构造对象'''
        url = HttpURL(self.url)
        self.assertEqual(url.protocol, 'https')
        self.assertEqual(url.path, '/')
        self.assertEqual(url.host, 'httpbin.org')
        self.assertEqual(url.port, HTTPS_PORT)

    def test_request_packet(self):
        '''3 测试url拼接'''
        url = HttpURL(self.url)
        self.assertEqual(url.request_packet, self.result)

    def test_client(self):
        '''4 测试http客户端创建'''
        url = HttpURL('https://httpbin.or/')
        self.assertRaises(SystemExit, HttpClient, url)
        url = HttpURL('http://httpbin.org/')
        client = HttpClient(url)
        self.assertIsInstance(client, HttpClient)
        client.sock.close()

    def tearDown(self):
        pass


if __name__ == '__main__':
    # unittest.main()
    main()

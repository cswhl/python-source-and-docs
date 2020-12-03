#! /usr/bin/python3

'''
description: 提取html中的链接
'''


from html.parser import HTMLParser
from io import StringIO
from urllib.request import urlopen
from urllib.parse import urljoin


def output(x):
    print('\n'.join(sorted(set(x))))


def htmlparser(url, f):
    'htmlparser() - use HTMLParser to parse anchor tags'
    class AnchorParser(HTMLParser):
        # This method is called to handle the start of a tag (e.g. <div
        # id="main">).
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            # judge HTMLParser instance's 'data' attribute
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    # add url' path
                    self.data.append(attr[1])
    # HTMLParser instances
    parser = AnchorParser()
    # Feed some text to the parser.
    parser.feed(f.read())
    # generator: join url and path, then output
    output(urljoin(url, x) for x in parser.data)


url = 'http://python.org'
f = urlopen(url)
data = StringIO(f.read().decode('utf-8'))
f.close()
htmlparser(url, data)

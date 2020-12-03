'''
description: 提取html中的链接
'''


from bs4 import BeautifulSoup
from io import StringIO
from urllib.request import urlopen
from urllib.parse import urljoin


def output(x):
    print('\n'.join(sorted(set(x))))


def fastBS(url, f):
    # make a BeautifulSoup objec, and filter with 'a', fetch the 'href' value,
    # return a generator
    output(urljoin(url, x['href']) for x in BeautifulSoup(f).find_all('a'))


url = 'http://python.org'
f = urlopen(url)
data = StringIO(f.read().decode('utf-8'))
f.close()
fastBS(url, data)

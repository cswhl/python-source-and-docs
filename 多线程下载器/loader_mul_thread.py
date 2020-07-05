# coding=utf-8
import requests
import time
from threading import Thread


class downloader(object):
    def __init__(self, url, thread_num):
        '''初始化要保存的文件名、url、线程数、文件长度'''
        self.name = url.split('/')[-1]
        self.url = url
        self.thread_num = thread_num
        res = requests.head(self.url)
        self.total_num = int(res.headers['Content-Length'])

    def get_blocks(self):
        '''按线程数量将文件划分为对应块'''
        # 1、块平均长度
        block_length = int(self.total_num / self.thread_num)

        # 2、将每个线程要下载的文件位置范围保存到元组中
        blocks = []
        for i in range(self.thread_num):
            start = i*block_length
            end = (i+1)*block_length if i+1 != self.thread_num else '' # ''代表最后一个块结束位置是未见末尾
            blocks.append((start, end))

        # 3、返回保存位置元组的列表
        return blocks

    def down_block(self, *start_end):
        '''下载文件块, 读取文件和写文件都是阻塞I/O'''
        headers = {'Range': 'Bytes= %s-%s' % start_end}
        res = requests.get(self.url, headers=headers)
        self.fd.seek(start_end[0])
        self.fd.write(res.content)

    def run(self):
        # with open(self.name, r'wb') as f:
        start_time = time.time()
        self.fd = open(self.name, r'wb')

        # 获取块数据，逐块写入
        threads = []
        for start_end in self.get_blocks():
            start, end = start_end
            thread = Thread(target=self.down_block, args=(start, end))
            thread.start()
            threads.append(thread)

        # 等待所有线程执行结束
        for thread in threads:
            thread.join()

        # 计算下载时间
        print(time.time() - start_time)
        self.fd.close()

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/static/image/timg.jpg'
    thread_num = 8
    down = downloader(url, thread_num)
    down.run()

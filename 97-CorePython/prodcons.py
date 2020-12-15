from random import randrange
from time import sleep
from queue import Queue
from myThread3 import MyThread

# 实现一个生产者-消费者模式
# 生产者向队列中放入数据，而消费者取出数据使用
def writeQ(queue):
    print('producing object for Q...', end='')
    queue.put('xxx', True) # 将'xxx‘放入队列
    print("size now", queue.qsize())

def readQ(queue):
    val = queue.get(1) # 从队列中获取item
    print('consumed object from Q... size now', queue.qsize())

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randrange(1, 4))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randrange(2, 6))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randrange(2, 6)
    q = Queue(32) # 初始化queue大小为32

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('all DONE')

if __name__ == '__main__':
    main()

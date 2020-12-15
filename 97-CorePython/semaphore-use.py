from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

# 使用锁和信号量模拟一个糖果机

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print('Refilling candy...', end=' ')
    try:
        candytray.release() # 释放一个资源
    except ValueError:
        print('full, skipping')
    else:
        print('OK')
    lock.release()

def buy():
    lock.acquire()
    print('Buying candy...', end=' ')
    if candytray.acquire(False): # 消耗一个资源，False代表非阻塞操作
        print('OK') # 获得资源则进入操作
    else:
        print('empty, skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('starting at:', ctime())
    nloops = randrange(2, 6)
    print('THE CANDY MACHINE (full with %d bars)!' % MAX)
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start() # buyer
    Thread(target=producer, args=(nloops,)).start() # vendor

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()

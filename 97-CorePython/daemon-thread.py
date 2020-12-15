from threading import Thread
from time import time, sleep

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        sleep(3)

t = Thread(target=countdown, args=(10,))
t.daemon = True # 设置为守护进程

t.start()
while True:
    if t.is_alive(): # 查询进程是否在运行
        print('still running') #
        sleep(3)
        break  # 主线程准备退出，因为仅有的子线程时守护线程，所以主线程就直接退出了

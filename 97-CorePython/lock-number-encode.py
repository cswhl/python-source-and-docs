from threading import Thread, Lock, local
from contextlib import contextmanager

_local = local() # 线程本地存储, thread-local storage


@contextmanager
def acquire(*locks):
    '''给每个锁分配唯一的编号，破坏死锁的环路等待条件的产生
    也可以用于检查可能存在的死锁情况：对锁的顺序做强制性约束，先获取到锁的对象ID必须比后获取的锁的ID要小
    '''
    locks = sorted((x_lock, y_lock), key=lambda x: id(x))  # 对lock排序

    acquired = getattr(_local, 'acquired', [])
    if acquired and max(acquired, key=lambda x: id(x)) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:  # 正序获取多个锁
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):  # 倒序释放锁
            lock.release()
        del acquired[-len(locks):]  # 删除之前添加的锁对象


x_lock = Lock()
y_lock = Lock()


def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')


def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')


t1 = Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = Thread(target=thread_2)
t2.daemon = True
t2.start()

import threading
from lock_number_encode import acquire

def thread_1():
    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print('Thread-1')


# 检测锁是否满足升序要求
# y_lock的id大于x_lock，不满足锁编号升序规则，报错
def thread_2():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print('Thread-2')


if __name__ == '__main__':
    x_lock = threading.Lock()
    y_lock = threading.Lock()
    t1 = threading.Thread(target=thread_1)
    t1.daemon = True
    t1.start()

    t2 = threading.Thread(target=thread_2)
    t2.daemon = True
    t2.start()

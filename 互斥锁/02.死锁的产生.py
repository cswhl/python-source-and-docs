import threading
import time


class MyThread(threading.Thread):
    def run(self):
        # 堆mutexA.acquire()
        mutexA.acquire()

        # mutexA上锁后，延迟一秒，等待另外线性把mutexB上锁
        print(self.name + '---do1---up---')
        time.sleep(1)

        # 此时会堵塞，因为mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()
        print(self.name + '---do2---down---')
        mutexB.release()

        # 堆mutexA解锁
        mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        # 堆mutexA.acquire()
        mutexB.acquire()

        # mutexA上锁后，延迟一秒，等待另外线性把mutexB上锁
        print(self.name + '---do2---up---')
        time.sleep(1)

        # 此时会堵塞，因为mutexA已经被另外的线程抢先上锁了
        mutexA.acquire()
        print(self.name + '---do2---down---')
        mutexA.release()

        # 堆mutexA解锁
        mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread2()
    t1.start()
    t2.start()

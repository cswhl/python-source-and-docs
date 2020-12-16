from threading import Thread, Condition
import time

# 实现一个周期性定时器，每当定时器超时时，其它的线程都可以感知到超时事件

class PeriodcTimer(object):
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = Condition()  # 创建Condition实例对象

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()  # 启动守护进程t

    def run(self):
        # 运行定时器，每个间隔通知等待中的线程
        while True:
            time.sleep(self._interval)  # 每当定时超时，其它线程便会感知到(由于notify_all通知)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()  # 唤醒全部等待self._cv Condition对象的线程

    def wait_for_tick(self):
        # 等待下个定时的tick
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()  # wait()主动释放锁并阻塞，等待被Condition对象的notify_all()唤醒


ptimer = PeriodcTimer(5)
ptimer.start()


def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1


def conutup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1


Thread(target=countdown, args=(10,)).start()
Thread(target=countdown, args=(5,)).start()

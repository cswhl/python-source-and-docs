from threading import Thread
from time import sleep

class CountdownTask(object):
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0: # 轮询退出状态，用于终止线程
            print('T-minus', n)
            n -= 1
            sleep(5)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()

c.terminate()
t.join

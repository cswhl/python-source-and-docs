from threading import Thread, RLock
import time

'''
引入了 Box 类，有 add() 方法和 remove() 方法，提供了进入 execute() 方法的入口。 execute() 的执行由 Rlock() 控
'''

class Box(object):
    lock = RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire() # 重入锁，调用execute的方法已经获取了锁
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()

def adder(box, items):
    while items > 0:
        print("adding 1 item in the box")
        box.add()
        time.sleep(1)
        items -= 1

def remover(box, items):
    while items > 0:
        print("removing item in the box")
        box.remove()
        time.sleep(1)
        items -= 1

if __name__ == "__main__":
    items = 5
    print(f"putting {items} items in the box")
    box = Box()
    t1 = Thread(target=adder, args=(box, items))
    t2 = Thread(target=remover, args=(box, items))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(f'{box.total_items} items still remain in the box')

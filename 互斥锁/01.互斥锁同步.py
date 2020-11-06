import threading
import time


g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        # mutex.acquire()  # 上锁
        with mutex:
            g_num += 1         # 该剧在执行的时候会解析成多句话，cpu会在执行到其中一句时将函数切出去，导致值没有及时保存 noqa
        # mutex.release()  # 解锁
    print("------test1 num=%d" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        # mutex.acquire()
        with mutex:
            g_num += 1         # 该剧在执行的时候会解析成多句话，cpu会在执行到其中一句时将函数切出去，导致值没有及时保存 noqa
        # mutex.release()
    print("------test2 num=%d" % g_num)


mutex = threading.Lock()
print(dir(mutex))


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    # 等待上面的2个线程执行完毕
    time.sleep(5)

    print("--- in main thread g_num%d---" % g_num)  # 最终显示结果并不是2000000


if __name__ == "__main__":
    main()

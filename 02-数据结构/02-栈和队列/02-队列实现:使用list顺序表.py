# coding=utf-8


class Queue(object):
    '''队列'''

    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        '''往队列中添加一个item元素'''
        self.__queue.append(item)

    def dequeue(self):
        '''出队列'''
        return self.__queue.pop(0)

    def is_empty(self):
        '''判断队列为空'''
        return self.__queue == []

    def size(self):
        '''队列的大小'''
        return len(self.__queue)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


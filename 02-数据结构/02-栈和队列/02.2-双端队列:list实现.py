# coding=utf-8


class DQueue(object):
    '''双端队列'''

    def __init__(self):
        self.__queue = []

    def add_front(self, item):
        '''往队列头添加一个item元素'''
        self.__queue.insert(0,item)

    def app_rear(self, item):
        '''往队列尾添加一个item元素'''
        self.__queue.append(item)

    def pop_front(self):
        '''从队列头删除一个元素'''
        return self.__queue.pop(0)

    def pop_rear(self):
        '''从队列尾删除一个元素'''
        return self.__queue.pop()

    def is_empty(self):
        '''判断队列为空'''
        return self.__queue == []

    def size(self):
        '''队列的大小'''
        return len(self.__queue)


if __name__ == '__main__':
    q = DQueue()

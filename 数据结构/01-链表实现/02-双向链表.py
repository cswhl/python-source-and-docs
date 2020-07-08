# coding=utf-8


class Node():
    '''结点类'''

    def __init__(self, elem):
        # 存放元素数据
        self.elem = elem
        # next是下一个节点的标识
        self.next = None
        # prev是前一个结点的标识
        self.prev = None


class Double_LinkList():
    '''链表类'''

    def __init__(self, node=None):
        # 头结点定义为私有变量
        self.__head = node

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head is None

    def length(self):
        '''获取链表的长度'''
        curr = self.__head
        # 查询结点到末尾
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def travel(self):
        '''遍历链表'''
        curr = self.__head
        # 查询结点到末尾
        while curr is not None:
            print(curr.elem)
            curr = curr.next

    def add(self, item):
        '''链表头部添加元素'''
        node = Node(item)
        node.next = self.__head
        self.__head = node
        if node.next is not None:
            node.next.prev = node

    def append(self, item):
        '''链表尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            curr = self.__head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            node.prev = curr

    def insert(self, pos, item):
        '''指定位置添加元素
        :param pos 从0开始
        '''
        pre = self.__head
        count = 0
        # 获取要插入位置前一个结点
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            while count < pos - 1:
                count += 1
                # curr = pre
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next.prev = node
            pre.next = node
            node.prev = pre

    def remove(self, item):
        '''删除节点'''
        pre = self.__head
        while pre is not None:
            if pre.elem is item:
                # 判断头结点删除
                if pre == self.__head:
                    self.__head = pre.next
                    if pre.next:
                        pre.next.prev = None
                else:
                    pre.prev.next = pre.next
                    if pre.next:
                        pre.next.prev = pre.prev
                break
            else:
                pre = pre.next

    def search(self, item):
        '''查找结点是否存在'''
        curr = self.__head
        while curr is not None:
            if curr.elem == item:
                return True
            curr = curr.next
        return False


if __name__ == '__main__':
    ll = Double_LinkList()
    ll.add(8)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert(11, 11)
    ll.remove(8)
    ll.travel()

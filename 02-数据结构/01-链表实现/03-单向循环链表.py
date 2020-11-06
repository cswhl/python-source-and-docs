class Node():
    '''结点类'''

    def __init__(self, elem):
        # 存放元素数据
        self.elem = elem
        # next是下一个节点的标识
        self.next = None


class Single_LoopLinkList():
    '''链表类'''

    def __init__(self, node=None):
        # 头结点定义为私有变量
        self.__head = node
        # node为结点时，next属性应指向自己
        if node:
            node.next = node

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head is None

    def length(self):
        '''获取链表的长度'''
        curr = self.__head
        # 空链表
        if self.is_empty():
            return 0
        # 从头结点之后开始查询，到头结点结束
        count = 1
        while curr.next is not self.__head:
            count += 1
            curr = curr.next
        return count

    def travel(self):
        '''遍历链表'''
        curr = self.__head
        # 空链表
        if self.is_empty():
            return
        # 从头结点之后开始查询，到头结点结束
        while curr.next is not self.__head:
            print(curr.elem, end=' ')
            curr = curr.next
        print(curr.elem, end=' ')

    def add(self, item):
        '''链表头部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 遍历到尾结点
            curr = self.__head
            while curr.next is not self.__head:
                curr = curr.next
            #  退出循环，指向尾结点
            curr.next = node
            node.next = self.__head
            self.__head = node

    def append(self, item):
        '''链表尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 遍历到尾结点
            curr = self.__head
            while curr.next is not self.__head:
                curr = curr.next
            #  退出循环，指向尾结点
            curr.next = node
            node.next = self.__head

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
            while count <  pos - 1:
                count += 1
                # curr = pre
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node


    def remove(self, item):
        '''删除节点'''
        pre = self.__head
        # 头结点删除处理
        if pre.elem is item:
            # 链表只有一个节点
            if pre.next is self.__head:
                self.__head = None
            else:
                # 遍历到尾节点
                curr = self.__head
                while curr.next is not self.__head:
                    curr = curr.next
                self.__head = pre.next
                curr.next = self.__head
            return
        # 中间和结点删除
        while pre.next is not self.__head:
            if pre.next.elem is item:
                pre.next = pre.next.next
                return
            else:
                pre = pre.next

    def search(self, item):
        '''查找结点是否存在'''
        # 空链表判断
        if self.is_empty():
            return False
        curr = self.__head
        while curr.next is not self.__head:
            if curr.elem == item:
                return True
            curr = curr.next
        if curr.elem == item:
            return True
        return False

if __name__ == '__main__':
    ll = Single_LoopLinkList()
    ll.add(8)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert(1,11)
    # ll.remove(8)
    ll.travel()

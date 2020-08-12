# coding=utf-8
'''
二分法的实现思路：
查找值在顺序表中对应的索引
1、每次迭代或递归都会将查询范围二分折半
2、值大于折半索引对应值时取右半区；值小于时取左半区；相等则返回折半索引值
'''

lis = [1, 3, 5, 6, 7, 9, 10, 12, 13, 15, 16, 17, 18]


def binary_search(key, li, start=0, end=None):
    '''
    二分法查找值在顺序表中的索引
    如果key不在顺序表中，返回最接近且小于key的值索引
    '''

    head = 0
    tail = len(li) - 1
    # 查找区域缩小到不超过两个数，退出循环
    while head < tail - 1:
        mid = (head + tail) // 2
        if key > li[mid]:
            # 大于时缩小一个范围
            head = mid + 1
        elif key < li[mid]:
            tail = mid
        else:
            return mid
        print(head, mid, tail)

    return head


def binary_search2(key, li, start=0, end=None):
    '''
    二分法查找值在顺序表中的索引
    如果key不在顺序表中，返回最接近且大于key的值索引
    '''

    head = 0
    tail = len(li) - 1
    while head < tail:
        mid = (head + tail) // 2
        if key > li[mid]:
            # 大于时缩小一个范围
            head = mid + 1
        elif key < li[mid]:
            # 小于时缩小一个范围
            tail = mid - 1
        else:
            return mid
        print(head, mid, tail)

    return head


def binary_search_recursion(key, li, start=0, end=None):
    '''
    二分法的递归实现: 查找得到的索引值层层返回获得
    '''
    if end is None:
        end = len(li) - 1

    print(start, end)
    if start < end - 1:
        num = (end - start) // 2 + start
        if key > li[num]:
            return binary_search_recursion(key, li, num + 1, end)
        elif key < li[num]:
            return binary_search_recursion(key, li, start, num)
        else:
            return num
    # key不在数组中，即返回最接近且小于它的值
    return start


print(binary_search_recursion(8, lis))

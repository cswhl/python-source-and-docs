'''
序列分为左无序，右有序(初始为空)
每次形成大顶堆后，将堆顶元素和无序序列的末尾元素互换
执行len(li)-1次后便形成有序序列

1、利用堆这种树形数据结构(父节点i的子节点2*i+1和2*i+2)形成大顶堆(最大元素在堆顶)
   父节点都大于子节点：父结点和子节点比较，子节点大于父节点时互换值
2、将堆顶元素和无序序列末尾元素互换,列表分为左无序，右有序(初始为空)
3、由于堆顶元素可能不是最大，重新将序列无序部分再次调整为大顶堆
4、重复步骤2~3，执行length-1次后得到有序序列，length为序列长度
'''
li = [6, 5, 3, 1, 8, 7, 9, 2, 4]


def heapfAjust(li, parent, length):
    '''递归:将序列调整为大顶堆'''
    # 从父节点、左右子节点查找最大元素
    largest, left, right = parent, parent*2 + 1, parent*2 + 2
    if left < length and li[left] > li[largest]:
        largest = left
    if right < length and li[right] > li[largest]:
        largest = right
    # 交换父子节点元素，对交换后的子节点递归:堆调整
    # 子节点都小于等于父节点时，递归结束
    if largest != parent:
        li[parent], li[largest] = li[largest], li[parent]
        heapfAjust(li, largest, length)


def heapySort(li):
    '''堆排序'''
    length = len(li)
    # 创建大顶堆
    for parent in range((length-2) // 2, -1, -1):
        heapfAjust(li, parent, length)
    # 循环len(li)-1次:将大顶堆顶元素放入无需序列的末尾(左部分无序，右部分有序)
    for last_p in range(length-1, 0, -1):
        # 堆顶元素和无序部分序列末尾元素互换
        li[0], li[last_p] = li[last_p], li[0]
        # 重新调整，恢复大顶堆特性
        heapfAjust(li, 0, last_p)
    return li


print(heapySort(li))


li = [6, 5, 3, 1, 8, 7, 9, 2, 4]


def heapfAjust_interable(li, parent, length):
    '''使用迭代调整为大顶堆'''
    largest, left = parent, parent*2 + 1
    while left < length:
        # 从父节点、左右子节点查找最大元素
        right = left + 1
        if right < length and li[right] > li[largest]:
            largest = right
        if li[left] > li[largest]:
            largest = left
        # 交换父子节点元素，对交换的子节点进行迭代：堆调整
        if largest != parent:
            li[parent], li[largest] = li[largest], li[parent]
            parent, left = largest, largest*2 + 1
        # 如果孩子节点小于或等于父节点，则结束
        else: break


def heapySort_interable(li):
    '''堆排序'''
    length = len(li)
    # 创建大顶堆
    for parent in range((length-2) // 2, -1, -1):
        heapfAjust_interable(li, parent, length)
    # 循环len(li)-1次:将大顶堆顶元素放入无需序列的末尾(左部分无序，右部分有序)
    for last_p in range(length-1, 0, -1):
        # # # 堆顶元素和无序部分序列末尾元素互换
        li[0], li[last_p] = li[last_p], li[0]
        # # # 重新调整，恢复大顶堆特性
        heapfAjust_interable (li, 0, last_p)
    return li


print(heapySort_interable(li))

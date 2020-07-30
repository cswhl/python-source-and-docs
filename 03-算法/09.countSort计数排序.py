

li = [6, 5, 0, 3, 1, 8, 7, 9, 2, 4, 4, 8]


def countSort(li):
    '''计数排序'''
    min, max = 0, 0
    # 获取最大和最小值
    for i in li:
        if i > max:
            max = i
        if i < min:
            min = i
    # 获取计数列表，下标=元素-min，值=元素出现次数
    ls = [0 for x in range(max - min + 1)]
    for i in li:
        ls[i - min] += 1
    # 计数累加:确定元素的在新数组中的存放位置
    for i in range(1, len(ls)):
        ls[i] += ls[i-1]
    # 重新汇总
    lib = [0 for x in range(len(li))]
    for j in li:
    # 元素实际位置需要减一，假使有元素0时其计数为1，填入位置为0=1-1
        lib[ls[j]-1] = j
        ls[j] -= 1

    return lib


print(countSort(li))

li = [6, 5, 0, 3, 1, 8, 7, 9, 2, 4, 4, 8]


def countSort_2(li):
    '''计数排序'''
    min, max = 0, 0
    # 获取最大和最小值
    for i in li:
        if i > max:
            max = i
        if i < min:
            min = i
    # 获取计数列表，下标=元素-min，值=元素出现次数
    ls = [0 for x in range(max - min + 1)]
    for i in li:
        # 使用i-min节省内存:不必从0开始分配
        ls[i - min] += 1
    # 将元素值重写入排序list
    m = 0
    for i in range(len(ls)):
        # 获取同一个元素的个数，并恢复元素值
        for j in range(ls[i]):
            li[m] = i + min
            m += 1
    return li


print(countSort_2(li))

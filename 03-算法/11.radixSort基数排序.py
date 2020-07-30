'''
一种多关键字的排序算法，``用桶排序实现:
将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零。然后，
从最低位开始，依次进行一次排序。这样从最低位排序一直到最高位排序完成以后，数列就变成一个有序序列

1 取得数组中最大数及数位的数量
2 从最低位开始
3 遍历序列：将元素放入其数位对应的桶号中；完成后将桶中元素倒出，便形成了按数位排序的序列
4 依次从次低位到最高位，重复步骤3；最高位排序完成就完成了排序
'''
li = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]

import math

def radixSort(li, radix=10):
    '''基数排序'''
    # 1、计数最大值位数
    num = int(math.ceil(math.log(max(li)+1, radix)))

    # 3、循环:以位数的大小对数据进行排序,最高位排序完成便得到有序序列
    for i in range(num):
        # 4、初始化桶，共0~9个桶
        buckets = [[] for j in range(radix)]
        for item in li:
            # 数位相同则装入同一个号桶
            buckets[item // radix**i % radix].append(item)
        del li[:]
        # 5、将该次按位排列的数据合并
        for bucket in buckets:
            li.extend(bucket)
    return li

radixSort(li)
print(li)

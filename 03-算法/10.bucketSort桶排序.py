'''
桶排序:
    假设输入数据服从均匀分布，将数据按划分的范围分别装入有限数量的桶中，每个桶再分别排序
    （有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排
    步骤:
    1 设置一个定量的数组当作空桶子(python:[[桶],[]..形式])
    2 寻访序列，并且把项目一个一个放到对应的桶子去。
    3 对每个不是空的桶子进行排序(使用归并排序或其它排序)
    4 从不是空的桶子里把项目再放回原来的序列中。

'''
li = [7, 12, 56, 23, 19, 33, 35, 42, 42, 2, 8, 22, 39, 26, 17]


def merge_sort(li):
    '''归并排序作为桶排序中每个桶的排序'''
    if len(li) < 2:
        return li
    mid = len(li) // 2
    left_li = merge_sort(li[:mid])
    right_li = merge_sort(li[mid:])

    result = []
    left_p, right_p = 0, 0
    while left_p < len(left_li) and right_p < len(right_li):
        if left_li[left_p] > right_li[right_p]:
            result.append(right_li[right_p])
            right_p += 1
        else:
            result.append(left_li[left_p])
            left_p += 1

    result += left_li[left_p:]
    result += right_li[right_p:]

    return result


def bucketSort(li):
    # 查找最小、最大值
    min, max = li[0], 0
    for i in li:
        if i > max:
            max = i
        if i < min:
            min = i

    # 确定桶的个数及范围
    bucketNum = 5
    # 确定桶的数据分布规模，如0号桶[min~min+average),1号桶[min+average, min+2*average)
    average = (max - min + 1) // bucketNum

    # 初始化桶
    buckets = []
    for i in range(bucketNum):
        buckets.append([])

    # 遍历将序列中元素放入对应的桶中,桶号=(i-min)/桶数据分布规模
    for i in li:
        buckets[(i - min) // average].append(i)

    # 对桶内元素进行排序,使用归并排序，也可使用其它排序
    for i in range(len(buckets)):
       buckets[i] =  merge_sort(buckets[i])

    # 将每个桶排序好的数据进行合并汇总放回原数组
    return [x for ls in buckets for x in ls]

li = bucketSort(li)
print(li)

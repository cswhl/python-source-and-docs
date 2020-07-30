'''
归并排序
递归：
1、把长度为n的输入序列分成两个长度为n/2的子序列；
2、重复:对两个子序列分别递归，直到子序列元素个数为1(最小有序序列)停止递归，
合并：
1、创建空list，合并两个子序列
2、逐个取左右序列元素比较：左序元素大于右序元素时，将右序元素加入list，否者将左序元素加入list
3、重复步骤2，直到将所有子序列全部合并完成()，return合并后的有序子序列
4、重复步骤1~3，直到合并完成所有子序列，最终返回元素序列的有序排序

迭代实现
将元素划分成单独序列后将相邻的序列合并排序：
1、初始视为每个元素都是一个子序列
2、将相邻的两个序列合并排序，合并完成后再继续合并下两个序列
3、重复步骤2，直到将所有序列都两两合并；序列数量减半，规模翻倍，存储合并后的序列
4、使用上次合并生成的序列，重复执行步骤2~3，完成排序
'''
li = [6, 5, 3, 1, 8, 7, 9, 2, 4]

layer = 0


def merge_iterate_sort(li):
    '''迭代实现'''

    # 序列规模:初始每个元素都是一个子序列，序列规模为1，相邻序列合并后规模翻倍>>
    for seg in [2**x for x in range(len(li) // 2)]:
        # 迭代获取要比较的相邻序列的起始位置
        buf = []
        # 要合并的相邻序列的起始地址
        for start in range(0, len(li), seg * 2):
            # 初始要合并的左右序列的各自的起始元素位置
            left, right = start, start + seg  # i是序列规模
            # 初始左右序列的最大范围, 不超过列表最大范围
            left_end, right_end = min(
                start + seg, len(li)), min(start + 2 * seg, len(li))

            # 左右序列合并
            while left < left_end and right < right_end:
                if li[left] < li[right]:
                    buf.append(li[left])
                    left += 1
                else:
                    buf.append(li[right])
                    right += 1
            buf += li[left:left_end]
            buf += li[right:right_end]
        li = buf
    return li


print(merge_iterate_sort(li))


def merge_sort(li):
    '''递归实现'''
    global layer
    if len(li) < 2:
        return li
    mid = len(li) // 2
    print(f'拆分数组:{li},拆分位置={mid}, 所在层次:{layer}')
    layer += 1
    print(f'拆分结果:{li[:mid]}  {li[mid:]} 所在层次:{layer} ')

    left_li = merge_sort(li[:mid])
    print(f'左返回数组={li[:mid]}, 所在层次:{layer}')
    right_li = merge_sort(li[mid:])
    print(f'右返回数组={li[mid:]}, 所在层次:{layer} \n')
    layer -= 1

    result = []
    left_p, right_p = 0, 0
    # 合并: 将返回的左右列表按顺序重排
    while left_p < len(left_li) and right_p < len(right_li):
        if left_li[left_p] > right_li[right_p]:
            result.append(right_li[right_p])
            right_p += 1
        else:
            result.append(left_li[left_p])
            left_p += 1

    # 将比较后剩余的部分元素添加到序列的末尾
    result += left_li[left_p:]
    result += right_li[right_p:]

    return result


# print(merge_sort(li))

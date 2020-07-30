'''
将全部元素用步长分成几个区域提升插入性能,
(步长：可以经计算得到或固定序列)
1、因为大步长可以让某个元素一次性向最终位置前进一大步
2、算法取越来越小的步长进行排序，最后一步步长为1就是插入排序
   到这步时，序列几乎已经排好了

希尔排序
1、初始步长为序列长度的一半
2、使用步长进行插入排序，完成后步长折半
3、重复步骤2，直到步长为1完成最后一次常规插入排序，排序完成
'''

li = [6, 5, 3, 1, 8, 7, 9, 2, 4]


def shell_sort(li):
    n = len(li)
    # gap是对元素分区的初始步长
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            # j = gap, gap+1, gap+2 ...
            i = j
            while i > 0:
                if li[i] < li[i - gap]:
                    li[i - gap], li[i] = li[i], li[i - gap]
                    i -= gap
                else:
                    break
            # print(f'li={li},gap={gap}')
        # 步长缩小一半
        gap //= 2


shell_sort(li)
print(f'结果:{li}')

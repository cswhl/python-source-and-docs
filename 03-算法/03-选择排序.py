

li = [1, 2, 3, 4, 5, 6, 7, 8]

def select_sort(li):
    length = len(li)
    # i:未排序部分的首位置
    for i in range(length-1):# 0~length-2,最后一位已排好序了，不用比了
        min_index = i
        # j:待比较元素的位置
        for j in range(i+1, length):
            if li[j] < li[min_index]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]


def selectSort(li):
    for i in range(len(li)):
        index = li.index(min(li[i:]))
        li[i], li[index] = li[index], li[i]

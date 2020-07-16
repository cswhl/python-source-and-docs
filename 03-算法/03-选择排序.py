'''
n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果。具体算法描述如下：
    初始状态：无序区为R[1..n]，有序区为空；
    第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。
    该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，
    使R[1..i]和R[i+1..n])分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
    n-1趟结束，数组有序化了。
'''

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

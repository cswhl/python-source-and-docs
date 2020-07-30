'''
快速排序
1、取list首元素为中位值，左游标值为表头，右游标为表尾
2、从右往左直到找到小于中位值的元素，将其放到左游标对应的位置，左游标+1
3、从左往右直到找到大于中位值得元素，将其放在右游标对应得位置，右游标+1
4、左游标<右游标时重复2~3步，直到左右游标相等时退出循环，将中位值放在当前左右游标位置，完成一次分区
5、对分区的左右部分进行递归排序：重复1~4步骤；当左游标>=右游标时停止递归

'''

li = [6, 5, 3, 1, 8, 7, 9, 2, 4]

def quick_sort(li, low, hight):
    '''快速排序'''

    # 退出递归：仅剩一个元素或无元素时
    if low >= hight: return
    # 取中位值
    left =low
    right = hight
    mid_value = li[left]

    # left和right相等时，小于中位值的在该位置左边,大于中位值的在该位置右边
    while left < right:
        # 从右往左找到小于等于中位值的元素，填入左端left位置
        while left < right and li[right] > mid_value:
            right -= 1
        li[left] = li[right]

        # 从左往右找到大于等于中位值的元素，填入右端right位置
        while left < right and li[left] < mid_value:
            left += 1
        li[right] = li[left]
    # 插入中位值
    li[left] = mid_value

    # 对low左边的执行快速排序
    quick_sort(li, low, left-1)
    # 对low右边的执行快速排序
    quick_sort(li, left+1, hight)



quick_sort(li, 0, len(li) - 1)
print(li)

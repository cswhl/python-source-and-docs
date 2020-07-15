'''
总体思路：
    待插入的元素的左边已排序(第一个元素被认为已排序)，右边没有排序：
    将右边首个元素插入左边比它小的元素之后，如此循环直到将右边元素全部填充到左边

# 常规思路
1、第一个元素可被认为已排序
2、取出下一个元素，从它左边已排序部分由后往前扫描元素
3、如果元素(已排序)大于它，则将元素移到下一位置
4、重复步骤3：
    a 直到查找元素小于它时，将它插入该元组位置(j)之后:(j+1)
    b 或 没有查找到比它小的元素，则将其插入头位置:0
5、重复步骤2~4):

# python的元组拆包思路：
利用python中的元组拆包，不断的将待插入元素以交换位置的方式向前移动：
    小于前一个元素就与其互换位置，最多移动次数为其当前所处的位置标号；
    当比前一个元素大时就break循环
'''
li = [6, 5, 3, 1, 8, 7, 2, 4]


def insert_sort(li):
    '''python的实现:使用元组拆包减少局部变量的使用'''
    for i in range(1, len(li)):
        j = i
        while j > 0:
            if li[j] < li[j-1]:
                # 交换位置：将小的元素往前移
                li[j-1], li[j] = li[j], li[j-1]
                j -= 1
            # 待插入元素小于前面的元素即退出循环
            else: break


def insertion_sort(li):
    '''不是很好的方案'''
    for i in range(1, len(li)):
        bak = li[i]
        j = i-1
        while j >= 0 and li[j] > bak:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = bak


# insertion_sort(li)
insert_sort(li)
print(li)


'''
1、比较相邻的元素。如果第一个比第二个大，就交换它们两个；
2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
3、针对所有的元素重复以上的步骤，除了最后一个；
4、重复步骤1~3，直到排序完成。
'''
li = [6, 5, 3, 1, 8, 7, 2, 4]

def bubble_sort(li):
    length = len(li)
    # 共走访length-1次，j为当前走访次数
    for j in range(length-1):
        count = 0
        # i：未排序队列中的用于相互比较的前一个元素位置
        for i in range(length-1-j):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                count += 1
        # 一次走访中从未互换过位置，说明已经排序完成
        if count == 0:break

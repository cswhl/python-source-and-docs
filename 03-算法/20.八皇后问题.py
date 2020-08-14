'''
八皇后问题:列出所有的方案
思路:使用生成器递归,总共遍历的次数为4**4
1、从第一行开始排列，每个皇后占一行
2、第一个皇后排第一列位置，递归调用
3、第二个皇后排第一列位置,出现冲突;递归结束，没有yield的值，所以该错误方案被弃

如此遍历及递归，如果最后一个皇后的位置也能确定，就代表这是一个正解，回退生成该方案
如果运行其中出现冲突，即抛弃该方案
'''
def conflict(state, nextX):
    '''处理冲突'''
    nextY = len(state)
    for i in range(nextY):
        # 1、同一在列:列差为0 2、在同一斜线上:列差和行差相等
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

def queen(num, state=()):
    '''递归生成器查询皇后排列:能确定最后一个皇后位置的才是正解'''
    for pos in range(num):
        if not conflict(state, pos):
            # 基线条件: 确定最后一个皇后的位置
            if len(state) == num-1:
                # 取列位置比较，行位置是确定的(从0开始，每个皇后占一行)
                yield (pos,)
            else:
                # 递归条件,queeem(num,stat+(pos,))在出现冲突时没有yield的值，这将抛弃冲突的方案
                for result in queen(num, state+(pos,)):
                    # 最后一个皇后确定时回退、连接生成正解
                    yield (pos,) + result


cc = list(queen(4))
print(cc)

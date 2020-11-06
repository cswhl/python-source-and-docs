# coding: utf-8


class Node(object):
    '''树节点'''

    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    '''二叉树'''

    def __init__(self):
        self.root = None

    def add(self, item):
        '''向二叉树上添加新节点'''
        node = Node(item)
        # 根节点为空
        if self.root is None:
            self.root = node
            return
        # 子节点不存在时赋值，已存在则向队列中该子节点
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        '''广度遍历'''
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')

            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, root):
        '''前序遍历:根左右'''
        # 递归结束:节点不存在则返回
        if root is None:
            return
        # 先显示父节点
        print(f'{root.elem}', end=' ')
        # 递归查询左子节点
        self.preorder(root.lchild)
        # 左子节点递归结束后继续递归查询右子节点
        self.preorder(root.rchild)

    def inorder(self, root):
        '''中序遍历:左根右'''
        if root is None:
            return

        # 递归查询左子节点
        self.inorder(root.lchild)
        # 左子节点递归结束后显示父节点
        print(f'{root.elem}', end=' ')
        # 继续递归查询右子节点
        self.inorder(root.rchild)

    def postorder(self, root):
        '''后序遍历:左右根'''
        if root is None:
            return

        # 递归查询左子节点
        self.postorder(root.lchild)
        # 继续递归查询右子节点
        self.postorder(root.rchild)
        # 左右子节点递归都结束后,显示父节点
        print(f'{root.elem}', end=' ')


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    print(f'广度遍历:', end=' ')
    tree.breadth_travel()
    print('\n')

    print(f'前序遍历:', end=' ')
    tree.preorder(tree.root)
    print('\n')

    print(f'中序遍历:', end=' ')
    tree.inorder(tree.root)
    print('\n')

    print(f'中序遍历:', end=' ')
    tree.postorder(tree.root)
    print('\n')

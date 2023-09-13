# -*- coding: utf-8 -*-
"""
@Time: 2023/9/12 17:16
@Author: GU Linghao
@File: binary_search_tree.py
@Description: 实现二叉搜索树
"""

class TreeNode():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val

        self.left = left
        self.right = right
        self.parent = parent

class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root

    def search(self, target_val):
        node = self.root

        while node:
            if node.val == target_val:
                return node
            elif node.val < target_val:
                node = node.left
            else:
                node = node.right
        return None

    def min(self, node=None):

        if not node:
            node = self.root

        while node.left:
            node = node.left
        return node

    def max(self, node=None):

        if not node:
            node = self.root

        while node.right:
            node = node.right
        return node


    def successor(self, node):
        '''
        给定一个节点，在二叉搜索树中寻找它的后继。如果该节点已是树中最大则返回None
        :param node:
        :return:
        '''

        if node.right:
            return self.min(node.right)
        else:
            # 向上，找到第一个左节点
            tmp = node.parent
            while tmp and node == tmp.right:
                node = tmp
                tmp = tmp.parent
            return tmp

    def predeceessor(self, node):
        '''
        给定一个节点，在二叉搜索树中寻找它的前驱。如果该节点已是书中最小则返回None
        :param node:
        :return:
        '''

        if node.left:
            return self.max(node.left)
        else:
            # 向上，找到第一个右节点
            tmp = node.parent
            while tmp and node == tmp.left:
                node = tmp
                tmp = tmp.parent
            return tmp

    def insert(self, node):
        x, y = self.root, None
        while x:
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right
        # root为None
        if not y:
            self.root = node
        # root不为None，根据Parent大小决定插入位置
        else:
            if node.val < y.val:
                y.left = node
            else:
                y.right = node
        node.parent = y

    def transplant(self, u, v):
        '''
        在二叉树中，用子树v替换子树u
        :param u:
        :param v:
        :return:
        '''

        # 如果u是根节点，直接替换
        if u == self.root:
            self.root = v
        # 否则根据u节点是左孩子还是右孩子，对应替换
        else:
            if u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
        # 最后更新双亲
        if v:
            v.parent = u.parent

    def delete(self, node):
        # 如果没有左孩子，直接用右孩子替换
        if not node.left:
            self.transplant(node, node.right)
        # 如果没有右孩子，直接用左孩子替换
        elif not node.right:
            self.transplant(node, node.left)
        # 有两个孩子
        else:
            y = self.min(node.right)
            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

def print_BST(bst):
    '''
    层序遍历二叉搜索树，用于检测输出情况
    :param bst:
    :return:
    '''

    ans = []

    def run(node, level):

        if len(ans) < level + 1:
            ans.append([])

        if node:
            ans[level].append(node.val)
            run(node.left, level + 1)
            run(node.right, level + 1)
        else:
            ans[level].append(None)

    run(bst.root, 0)
    print(ans)


node0, node1, node2, node3, node4 = TreeNode(12), TreeNode(5), TreeNode(18), TreeNode(2), TreeNode(9)
node5, node6, node7, node8 = TreeNode(15), TreeNode(19), TreeNode(13), TreeNode(17)

bst = BinarySearchTree(node0)
bst.insert(node1)
bst.insert(node2)
bst.insert(node3)
bst.insert(node4)
bst.insert(node5)
bst.insert(node6)
print_BST(bst)

print(bst.successor(node1))
print(bst.predeceessor(node4))

bst.delete(node2)
print_BST(bst)






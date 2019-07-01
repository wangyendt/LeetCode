# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/6/19 18:31
# software: PyCharm

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.height = 0


def maxDepth(root: TreeNode) -> int:
    def recursive(tr, dep):
        if not tr:
            return dep
        else:
            return max(recursive(tr.left, dep + 1), recursive(tr.right, dep + 1))

    return recursive(root, 0)


def parseTreeNode(l):
    if not l:
        return None
    tree = TreeNode(l[0])
    leaves = [tree]
    l.pop(0)
    while l:
        leavesTmp = []
        for t in leaves:
            if l[0] == 'null':
                t.left = None
            else:
                t.left = TreeNode(l[0])
                leavesTmp.append(t.left)
            l.pop(0)
            if l:
                if l[0] == 'null':
                    t.right = None
                else:
                    t.right = TreeNode(l[0])
                    leavesTmp.append(t.right)
                l.pop(0)
            if not l:
                break
            leaves = leavesTmp
    return tree


def showTreeNode(tree: TreeNode):
    stack = [tree]
    ret = []
    while stack and len(ret) < 2 ** maxDepth(tree) - 1:
        tr = stack.pop(0)
        if not tr:
            ret.append('null')
            stack.append(None)
            stack.append(None)
        else:
            ret.append(tr.val)
            stack.append(tr.left)
            stack.append(tr.right)
    return ret


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def _update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def _unbalance(self, node):
        return abs(self.height(node.left) - self.height(node.right)) is 2

    """右旋处理LL"""

    def _right_rotate(self, node):
        node_right = node
        node = node.left
        node_right.left = node.right
        node.right = node_right

        self._update_height(node_right)
        self._update_height(node)

        return node

    """左旋处理RR"""

    def _left_rotate(self, node):
        node_left = node
        node = node.right
        node_left.right = node.left
        node.left = node_left

        self._update_height(node_left)
        self._update_height(node)

        return node

    """双向旋转（先左后右）平衡处理LR"""

    def _left_right_rotate(self, node):
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    """双向旋转（先右后左）平衡处理RL"""

    def _right_left_rotate(self, node):
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

    """插入元素"""

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.root = self._insert(val, self.root)

    def _insert(self, val, node):
        if node is None:
            node = TreeNode(val)

        elif val < node.val:  # 左侧插入结点
            node.left = self._insert(val, node.left)
            if self._unbalance(node):  # 不平衡
                if val < node.left.val:  # LL不平衡
                    node = self._right_rotate(node)  # 右旋
                else:  # LR不平衡
                    node = self._left_right_rotate(node)  # 先左旋再右旋

        elif val > node.val:  # 右侧插入结点
            node.right = self._insert(val, node.right)
            if self._unbalance(node):  # 不平衡
                if val < node.right.val:  # LR不平衡
                    node = self._right_left_rotate(node)  # 先右旋再左旋
                else:  # RR不平衡
                    node = self._left_rotate(node)  # 左旋

        self._update_height(node)

        return node

    # 查询val在树中介于哪两个数字之间
    def query(self, val: int) -> (int, int):
        p = self.root
        while p:
            if val < p.val:
                if p.left:
                    if val < p.left.val:
                        p = p.left
                    else:
                        return p.left.val, p.val
                else:
                    return -1, p.val
            else:
                if p.right:
                    if val > p.right.val:
                        p = p.right
                    else:
                        return p.val, p.right.val
                else:
                    return p.val, -1
        return -1, -1

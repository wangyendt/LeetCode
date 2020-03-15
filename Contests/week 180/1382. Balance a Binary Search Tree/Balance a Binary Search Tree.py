#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/15 16:21
@Author:  wang121ye
@File: Balance a Binary Search Tree.py
@Software: PyCharm
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def traverse(tree: TreeNode):
            if tree:
                elements.append(tree.val)
                traverse(tree.left)
                traverse(tree.right)

        def make_bbt(tree: TreeNode, items: list):
            n = len(items)
            tree.val = items.pop(n // 2)
            if n >= 2:
                tree.left = TreeNode(0)
                make_bbt(tree.left, items[:n // 2])
            if n >= 3:
                tree.right = TreeNode(0)
                make_bbt(tree.right, items[n // 2:])

        elements = []
        traverse(root)
        elements.sort()
        ret = TreeNode(0)
        make_bbt(ret, elements)
        return ret

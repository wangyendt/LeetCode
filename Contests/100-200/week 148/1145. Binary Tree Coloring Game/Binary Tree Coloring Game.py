#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Binary Tree Coloring Game
@time: 2019/8/14 15:20
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def findX(tree: TreeNode):
            if tree:
                if tree.val == x:
                    return tree
                else:
                    return findX(tree.left) or findX(tree.right)
            else:
                return None

        def get_node_sum(tree):
            if not tree:
                return 0
            else:
                return 1 + get_node_sum(tree.left) + get_node_sum(tree.right)

        nodeX = findX(root)
        a, b = get_node_sum(nodeX.left), get_node_sum(nodeX.right)
        c = n - (a + b + 1)
        return max(a, b, c) * 2 > n


so = Solution()
root = parseTreeNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(so.btreeGameWinningMove(root, 11, 3))

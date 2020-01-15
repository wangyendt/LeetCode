#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Sum of Nodes with Even-Valued Grandparent
@time: 2020/1/15 14:56
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ret = [0]

        def helper(tree: TreeNode):
            def find_grandson(tree: TreeNode, lvl=2):
                if not tree: return
                if lvl == 0:
                    ret[0] += tree.val
                else:
                    find_grandson(tree.left, lvl - 1)
                    find_grandson(tree.right, lvl - 1)

            if not tree: return

            if tree.val % 2 == 0:
                find_grandson(tree)
            helper(tree.left)
            helper(tree.right)

        helper(root)
        return ret[0]


so = Solution()
null = 'null'
tree = parseTreeNode([6, 7, 8, 2, 7, 1, 3, 9, null, 1, 4, null, null, null, 5])
print(so.sumEvenGrandparent(tree))

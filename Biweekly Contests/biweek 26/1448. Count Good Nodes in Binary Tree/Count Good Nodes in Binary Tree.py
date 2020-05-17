#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/17 17:13
@Author:  wang121ye
@File: Count Good Nodes in Binary Tree.py
@Software: PyCharm
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ret = 0
        self.helper(root, -sys.maxsize)
        return self.ret

    def helper(self, tree: TreeNode, max_val: int):
        if not tree: return 0
        # print(tree.val, max_val)
        if tree.val >= max_val:
            self.ret += 1
            max_val = tree.val
        self.helper(tree.left, max_val)
        self.helper(tree.right, max_val)


null = 'null'
so = Solution()
print(so.goodNodes(parseTreeNode([3, 1, 4, 3, null, 1, 5])))
print(so.goodNodes(parseTreeNode([3, 3, null, 4, 2])))
print(so.goodNodes(parseTreeNode([1])))

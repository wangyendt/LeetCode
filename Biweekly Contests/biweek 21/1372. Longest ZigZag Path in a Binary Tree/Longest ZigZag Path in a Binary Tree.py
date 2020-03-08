#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/8 19:44
@Author:  wang121ye
@File: Longest ZigZag Path in a Binary Tree.py
@Software: PyCharm
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(root):
            if not root: return [-1, -1, -1]
            left, right = dfs(root.left), dfs(root.right)
            return [left[1] + 1, right[0] + 1, max(left[1] + 1, right[0] + 1, left[2], right[2])]

        return dfs(root)[-1]

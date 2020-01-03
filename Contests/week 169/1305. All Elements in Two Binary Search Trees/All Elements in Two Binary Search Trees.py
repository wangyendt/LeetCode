#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: All Elements in Two Binary Search Trees
@time: 2020/1/3 15:07
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *
import heapq


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list:
        ret = []

        def helper(tree: TreeNode):
            if not tree: return
            heapq.heappush(ret, tree.val)
            helper(tree.left)
            helper(tree.right)

        helper(root1)
        helper(root2)
        return [heapq.heappop(ret) for _ in ret]

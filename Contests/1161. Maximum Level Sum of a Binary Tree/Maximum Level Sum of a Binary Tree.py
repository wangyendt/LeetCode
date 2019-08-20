#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Level Sum of a Binary Tree
@time: 2019/8/20 15:25
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *
import collections


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sum_dict = collections.defaultdict(int)

        def helper(tree: TreeNode, level=1):
            if not tree:
                return
            level_sum_dict[level] += tree.val
            helper(tree.left, level + 1)
            helper(tree.right, level + 1)

        helper(root)
        print(level_sum_dict.items())

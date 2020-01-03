#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Deepest Leaves Sum
@time: 2020/1/3 14:51
"""

import sys

sys.path.append('..')
from Tools.BinaryTree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deepest_node_dict = collections.defaultdict(list)

        def helper(tree: TreeNode, level):
            if not tree: return
            if not tree.left and not tree.right:
                deepest_node_dict[level].append(tree.val)
                return
            helper(tree.left, level + 1)
            helper(tree.right, level + 1)

        helper(root, 0)
        return sum(deepest_node_dict[max(deepest_node_dict.keys())])

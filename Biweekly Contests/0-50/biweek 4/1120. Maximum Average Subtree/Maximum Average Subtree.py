#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Maximum Average Subtree.py 
@time: 2019/07/13
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

sys.path.append('..')
from Tools.BinaryTree import *


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        ret = [-sys.maxsize]

        def helper(tree):
            if not tree:
                return 0, 0
            else:
                if not tree.left and not tree.right:
                    ret[0] = max(ret[0], float(tree.val))
                    return tree.val, 1
                else:
                    left = helper(tree.left)
                    right = helper(tree.right)
                    Sum = left[0] + right[0] + tree.val
                    Count = left[1] + right[1] + 1
                    ret[0] = max(ret[0], Sum / Count)
                    return Sum, Count

        helper(root)
        return ret[0]


tree = parseTreeNode([5, 6, 1])
tree = parseTreeNode([0, 'null', 1])
so = Solution()
print(so.maximumAverageSubtree(tree))

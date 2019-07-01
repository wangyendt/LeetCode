#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Binary Tree Maximum Path Sum.py 
@time: 2019/07/02
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

sys.path.append('../Tools')
from Tools.BinaryTree import *


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        dp = []

        def helper(tree):
            if not tree:
                return 0
            if not tree.left and not tree.right:
                dp.append(tree.val)
                return max(tree.val, 0)
            l, r = helper(tree.left), helper(tree.right)
            lM = l + tree.val
            rM = r + tree.val
            M = max(lM, rM, l + r + tree.val, tree.val)
            dp.append(M)
            return max(l + tree.val, r + tree.val)

        helper(root)
        print(dp)
        return max(dp)


tree = parseTreeNode([7, -3, -6, -7, 'null', -6, 'null', 'null', -8, 'null', 4, 'null', -4])
so = Solution()
print(so.maxPathSum(tree))

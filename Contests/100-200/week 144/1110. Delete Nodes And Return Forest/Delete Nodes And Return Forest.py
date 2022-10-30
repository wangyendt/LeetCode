#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Delete Nodes And Return Forest.py 
@time: 2019/07/07
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
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

class Solution:
    def delNodes(self, root: TreeNode, to_delete: list) -> list:
        if not root:
            return []
        if not to_delete:
            return [root]
        ret = []
        stack = [(TreeNode(to_delete[0]), root, 0)]
        while stack:
            father, child, gender = stack.pop()
            if child:
                stack.append((child, child.left, 0))
                stack.append((child, child.right, 1))
                if child.val in to_delete:
                    if gender == 0:
                        father.left = None
                    else:
                        father.right = None
                else:
                    if father.val in to_delete:
                        ret.append(child)
        return ret


tree = parseTreeNode([1, 2, 3, 4, 5, 6, 7])
so = Solution()
ret = so.delNodes(tree, [3, 5])
[print(showTreeNode(r)) for r in ret]

tree = parseTreeNode([1, 2, 3, 'null', 'null', 'null', 4])
so = Solution()
ret = so.delNodes(tree, [2, 1])
[print(showTreeNode(r)) for r in ret]

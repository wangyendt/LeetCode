#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Nodes Equal to Average of Subtree.py 
@time: 2022/05/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ret = 0

        def helper(tree: TreeNode):
            if not tree: return 0, 0
            l1, l2 = helper(tree.left)
            r1, r2 = helper(tree.right)
            avg = (tree.val + l2 + r2) // (1 + l1 + r1)
            if avg == tree.val:
                self.ret += 1
            return l1 + r1 + 1, l2 + r2 + tree.val

        helper(root)
        return self.ret

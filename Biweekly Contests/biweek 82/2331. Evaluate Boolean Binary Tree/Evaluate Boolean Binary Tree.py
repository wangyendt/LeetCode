#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Evaluate Boolean Binary Tree.py 
@time: 2022/07/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def helper(tree):
            if not (tree.left or tree.right):
                return bool(tree.val)
            if tree.val == 2:
                return helper(tree.left) or helper(tree.right)
            elif tree.val == 3:
                return helper(tree.left) and helper(tree.right)

        return helper(root)

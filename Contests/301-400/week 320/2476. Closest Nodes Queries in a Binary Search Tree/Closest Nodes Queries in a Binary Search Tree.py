#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Closest Nodes Queries in a Binary Search Tree.py 
@time: 2022/11/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect
import sys

sys.path.append('../..')
from Tools.BinaryTree import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        res = set()

        def helper(tree: TreeNode):
            if tree:
                res.add(tree.val)
                helper(tree.left)
                helper(tree.right)

        helper(root)
        res = list(sorted(list(res)))
        ret = []
        for q in queries:
            idx = bisect.bisect_right(res, q)
            if idx == 0:
                mn = -1
            else:
                mn = res[idx - 1]
            idx = bisect.bisect_left(res, q)
            if idx == len(res):
                mx = -1
            else:
                mx = res[idx]
            ret.append([mn, mx])
        return ret


null = 'null'
tree = parseTreeNode([6, 2, 13, 1, 4, 9, 15, null, null, null, null, null, null, 14])
so = Solution()
print(so.closestNodes(tree, queries=[2, 5, 16]))

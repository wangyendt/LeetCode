#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Operations to Sort a Binary Tree by Level.py 
@time: 2022/11/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import sys

sys.path.append('../..')
from Tools.BinaryTree import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def get_min_swap(A: list):
            B = sorted(A)
            m = collections.defaultdict(int)
            l = len(A)
            for i in range(l):
                m[B[i]] = i
            loops = 0
            flag = [False] * l
            for i in range(l):
                if not flag[i]:
                    j = i
                    while not flag[j]:
                        flag[j] = True
                        j = m[A[j]]
                    loops += 1
            return l - loops

        nodes = collections.defaultdict(list)

        def helper(tree: TreeNode, level):
            if tree:
                nodes[level].append(tree.val)
                helper(tree.left, level + 1)
                helper(tree.right, level + 1)

        helper(root, 0)
        ret = 0
        for k, v in nodes.items():
            ret += get_min_swap(v)
        return ret


root = [1, 3, 2, 7, 6, 5, 4]
root = parseTreeNode(root)
so = Solution()
print(so.minimumOperations(root))

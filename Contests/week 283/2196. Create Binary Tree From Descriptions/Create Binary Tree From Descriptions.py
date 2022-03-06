#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Create Binary Tree From Descriptions.py 
@time: 2022/03/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        res = collections.defaultdict(TreeNode)
        has_father = collections.defaultdict(bool)
        root_candidates = set()
        for p, c, is_left in descriptions:
            root_candidates.add(p)
            has_father[c] = True
            if c not in res:
                res[c] = TreeNode(c)
            if p not in res:
                res[p] = TreeNode(p)
                if is_left:
                    res[p].left = res[c]
                else:
                    res[p].right = res[c]
            else:
                if is_left:
                    res[p].left = res[c]
                else:
                    res[p].right = res[c]
        for rc in root_candidates:
            if not has_father[rc]:
                return res[rc]

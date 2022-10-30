#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Step-By-Step Directions From a Binary Tree Node to Another.py 
@time: 2021/12/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import sys

sys.path.append('../../..')
from Tools.BinaryTree import *


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getDirections(self, root, startValue, destValue) -> str:
        # def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        tree = root

        def helper(tree_, p_, q_):
            if not tree_ or tree_.val == p_ or tree_.val == q_: return tree_
            left = helper(tree_.left, p_, q_)
            right = helper(tree_.right, p_, q_)
            if left and right:
                return tree_
            elif left:
                return left
            elif right:
                return right
            return None

        tree_res = dict()

        def traverse(tree_, q_):
            if not tree_: return
            if tree_.val in q_:
                tree_res[q_[tree_.val]] = tree_
            traverse(tree_.left, q_)
            traverse(tree_.right, q_)

        query = {
            startValue: 'start',
            destValue: 'des'
        }
        ancestor = helper(tree, startValue, destValue).val
        if ancestor != startValue and ancestor != destValue:
            query[ancestor] = 'anc'
        traverse(tree, query)

        def find(p_, q_):
            if not p_: return []
            if p_.val == q_.val:
                return ['O']
            res = find(p_.left, q_)
            if res:
                res[0:0] = ['L']
                return res
            res = find(p_.right, q_)
            if res:
                res[0:0] = ['R']
                return res
            return []

        path = ''
        if ancestor == startValue:
            path = find(tree_res['start'], tree_res['des'])
            path = ''.join(path)[:-1]
            # print(path)
        elif ancestor == destValue:
            path = find(tree_res['des'], tree_res['start'])
            path = 'U' * (len(path) - 1)
            # print(path)
        else:
            path1 = find(tree_res['anc'], tree_res['start'])
            path2 = find(tree_res['anc'], tree_res['des'])
            # print(path1, path2)
            path = 'U' * (len(path1) - 1) + ''.join(path2[:-1])
            # print(path)
        return path


null = 'null'
so = Solution()
t = parseTreeNode([5, 1, 2, 3, null, 6, 4])
print(so.getDirections(t, 3, 5))
print(so.getDirections(t, 5, 3))
print(so.getDirections(t, 3, 6))
t = parseTreeNode([2, 1])
print(so.getDirections(t, 2, 1))

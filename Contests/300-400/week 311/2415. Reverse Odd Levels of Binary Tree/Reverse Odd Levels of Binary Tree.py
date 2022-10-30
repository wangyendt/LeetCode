#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Reverse Odd Levels of Binary Tree.py 
@time: 2022/09/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import sys

sys.path.append('..')
from Tools.BinaryTree import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = collections.defaultdict(list)

        def helper(tree: TreeNode, level=0):
            if tree:
                nodes[level].append(tree.val)
                helper(tree.left, level + 1)
                helper(tree.right, level + 1)

        helper(root)
        for i in nodes:
            if i & 1:
                nodes[i] = nodes[i][::-1]

        def helper2(tree: TreeNode, level=0):
            if level in nodes:
                if level == 0:
                    tree.val = nodes[0][0]
                else:
                    tree.left = TreeNode(nodes[level].pop(0), level + 1)
                    helper2(tree.left)
                    tree.right = TreeNode(nodes[level].pop(0), level + 1)
                    helper2(tree.right)

        res = []
        for i in nodes:
            for j in nodes[i]:
                res.append(j)
        tree = TreeNode(res[0])
        leaves = [tree]
        res.pop(0)
        while res:
            leavesTmp = []
            for t in leaves:
                if res[0] == 'null':
                    t.left = None
                else:
                    t.left = TreeNode(res[0])
                    leavesTmp.append(t.left)
                res.pop(0)
                if res:
                    if res[0] == 'null':
                        t.right = None
                    else:
                        t.right = TreeNode(res[0])
                        leavesTmp.append(t.right)
                    res.pop(0)
                if not res:
                    break
                leaves = leavesTmp
        return tree


tree = parseTreeNode([2, 3, 5, 8, 13, 21, 34])
print(showTreeNode(tree))
so = Solution()
print(so.reverseOddLevels(tree))

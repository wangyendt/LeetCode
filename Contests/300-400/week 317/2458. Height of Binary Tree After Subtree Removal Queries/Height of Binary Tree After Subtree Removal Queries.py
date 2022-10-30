#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Height of Binary Tree After Subtree Removal Queries.py 
@time: 2022/10/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, R: Optional[TreeNode], Q: List[int]) -> List[int]:
        Depth, Height = collections.defaultdict(int), collections.defaultdict(int)

        def dfs(node, depth):
            if not node:
                return -1
            Depth[node.val] = depth
            cur = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1)) + 1
            Height[node.val] = cur
            return cur

        dfs(R, 0)

        cousins = {}
        for val, depth in Depth.items():
            if depth not in cousins:
                cousins[depth] = []
            heapq.heappush(cousins[depth], (-Height[val], val))

        ans = []
        for q in Q:
            depth = Depth[q]
            if len(cousins[depth]) == 1:
                ans.append(depth - 1)
            elif cousins[depth][0][1] == q:
                tmp = heapq.heappop(cousins[depth])
                ans.append(-cousins[depth][0][0] + depth)
                heapq.heappush(cousins[depth], tmp)
            else:
                ans.append(-cousins[depth][0][0] + depth)
        return ans


import sys

sys.path.append('../../..')
from Tools.BinaryTree import *

tree = parseTreeNode([5, 8, 9, 2, 1, 3, 7, 4, 6])
so = Solution()
print(so.treeQueries(tree, [3, 2, 4, 8]))

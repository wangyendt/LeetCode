#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Nodes With the Highest Score.py 
@time: 2021/10/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        tree = collections.defaultdict(list)
        for i, p in enumerate(parents):
            tree[p].append(i)
        # print(tree)
        cnter = collections.defaultdict(dict)

        def helper(node: int):
            if not tree[node]:
                cnter[node][0] = cnter[node][1] = 0
            elif len(tree[node]) == 1:
                cnter[node][0] = helper(tree[node][0])
                cnter[node][1] = 0
            else:
                cnter[node][0] = helper(tree[node][0])
                cnter[node][1] = helper(tree[node][1])
            return 1 + cnter[node][0] + cnter[node][1]

        helper(-1)
        # print(cnter)
        # print(n)
        ans = collections.defaultdict(int)
        for i in range(n):
            if cnter[i][0] == cnter[i][1] == 0:
                ret = n - 1
            if cnter[i][0] != 0 and cnter[i][1] == 0:
                ret = cnter[i][0] * ((n - 1 - cnter[i][0]) if n - 1 - cnter[i][0] != 0 else 1)
            if cnter[i][0] == 0 and cnter[i][1] != 0:
                ret = cnter[i][1] * ((n - 1 - cnter[i][1]) if n - 1 - cnter[i][1] != 0 else 1)
            if cnter[i][0] != 0 and cnter[i][1] != 0:
                ret = cnter[i][0] * cnter[i][1] * (
                    (n - cnter[i][0] - cnter[i][1] - 1)
                    if (n - cnter[i][0] - cnter[i][1] - 1) != 0 else 1
                )
            ans[ret] += 1
        # print(ans)
        return sorted(ans.items(), key=lambda x: x[0])[-1][1]


so = Solution()
print(so.countHighestScoreNodes(parents=[-1, 2, 0, 2, 0]))
print(so.countHighestScoreNodes(parents=[-1, 2, 0]))

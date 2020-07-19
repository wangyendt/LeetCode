#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Nodes in the Sub-Tree With the Same Label
@time: 2020/07/20 00:20
"""

import collections


class Solution:
    def countSubTrees(self, n: int, edges: list(list()), labels: str) -> list:
        neighbor = collections.defaultdict(list)
        for p, q in edges:
            neighbor[p].append(q)
            neighbor[q].append(p)
        ret = [0] * n

        def helper(i, cnter, parent):
            for nei in neighbor[i]:
                if nei != parent:
                    res = helper(nei, collections.defaultdict(int), i)
                    for v in res:
                        cnter[v] += res[v]
            cnter[labels[i]] += 1
            ret[i] = cnter[labels[i]]
            return cnter

        helper(0, collections.defaultdict(int), -1)
        return ret


so = Solution()
print(so.countSubTrees(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], labels="abaedcd"))
print(so.countSubTrees(n=4, edges=[[0, 1], [1, 2], [0, 3]], labels="bbbb"))
print(so.countSubTrees(n=5, edges=[[0, 1], [0, 2], [1, 3], [0, 4]], labels="aabab"))
print(so.countSubTrees(n=6, edges=[[0, 1], [0, 2], [1, 3], [3, 4], [4, 5]], labels="cbabaa"))
print(so.countSubTrees(n=7, edges=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]], labels="aaabaaa"))

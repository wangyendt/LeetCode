#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Kth Ancestor of a Tree Node
@time: 2020/06/14 11:48
"""

import collections


class TreeAncestor:

    def __init__(self, n: int, parent: list):
        dic = collections.defaultdict(list)
        for c, p in enumerate(parent):
            dic[p].append(c)
        self.memo = {}  # (node, #above) : node

        # store 1, 2, 4, etc above myself
        def dfs(curr, lst):
            j = 1
            while j <= len(lst):
                self.memo[curr, j] = lst[-j]
                j *= 2
            lst.append(curr)
            for nxt in dic[curr]:
                dfs(nxt, lst)
            lst.pop()

        dfs(0, [])

    def getKthAncestor(self, node: int, k: int) -> int:
        currPow = 1
        while k > 0:
            if k & 1:
                if (node, currPow) not in self.memo:
                    return -1
                node = self.memo[node, currPow]
            currPow *= 2
            k >>= 1
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

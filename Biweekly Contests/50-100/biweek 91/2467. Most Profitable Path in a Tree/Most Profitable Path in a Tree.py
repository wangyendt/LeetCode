#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Most Profitable Path in a Tree.py 
@time: 2022/11/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import sys

sys.setrecursionlimit(1000000)


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjList = collections.defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        n = len(adjList)
        time = [0] * n
        time[bob] = 1

        # dfs to calculate time to reach node from bob
        def dfs1(node, par):
            if node == bob:
                return time[bob]
            res = 0
            for adj in adjList[node]:
                if adj == par:
                    continue
                flag = dfs1(adj, node)
                if flag != 0:
                    res = 1 + flag
            time[node] = res
            return time[node]

        dfs1(0, None)

        self.res = float("-inf")

        def dfs2(node, par, t, income):
            for adj in adjList[node]:
                if adj == par:
                    continue
                newTime = t + 1
                newIncome = income
                if time[adj] == 0 or newTime < time[adj]:
                    newIncome += amount[adj]
                elif newTime == time[adj]:
                    newIncome += amount[adj] // 2
                if len(adjList[adj]) == 1:
                    self.res = max(self.res, newIncome)
                dfs2(adj, node, newTime, newIncome)

        dfs2(0, None, 1, amount[0])
        return self.res


so = Solution()
print(so.mostProfitablePath(edges=[[0, 1], [1, 2], [1, 3], [3, 4]], bob=3, amount=[-2, 4, 2, -4, 6]))
print(so.mostProfitablePath(edges=[[0, 1]], bob=1, amount=[-7280, 2350]))
print(so.mostProfitablePath([[0, 2], [0, 5], [1, 3], [1, 5], [2, 4]], 4, [5018, 8388, 6224, 3466, 3808, 3456]))
print(so.mostProfitablePath([[i, i + 1] for i in range(100000)], 50000, [0] * 100000))

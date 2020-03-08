#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/8 21:00
@Author:  wang121ye
@File: Frog Position After T Seconds.py
@Software: PyCharm
"""


class Solution:
    def frogPosition(self, n: int, edges: list(list()), t: int, target: int) -> float:
        if n == 1: return 1.0
        G = [[] for i in range(n + 1)]
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
        seen = [0] * (n + 1)

        def dfs(i, t):
            if i != 1 and len(G[i]) == 1 or t == 0:
                return i == target
            seen[i] = 1
            res = sum(dfs(j, t - 1) for j in G[i] if not seen[j])
            return res * 1.0 / (len(G[i]) - (i != 1))

        return dfs(1, t)

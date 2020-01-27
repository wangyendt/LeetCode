#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Find the City With the Smallest Number of Neighbors at a Threshold Distance
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/26 10:54
@Desc   ：
=================================================="""

import collections


class Solution:
    def findTheCity(self, n: int, edges: list(list()), distanceThreshold: int) -> int:
        def floyd_warshall(G_: dict):
            for k in G_.keys():
                for i in G_.keys():
                    for j in G_[i].keys():
                        if G_[i][j] > G_[i][k] + G_[k][j]:
                            G_[i][j] = G_[i][k] + G_[k][j]
                            # G_[j][i] = G_[i][j]

        edges = [e for e in edges if e[2] <= distanceThreshold]
        G = collections.defaultdict(dict)
        inf = 100000
        for i in range(n):
            for j in range(n):
                G[i][j] = 0 if i == j else inf
        for e1, e2, e3 in edges:
            G[e1][e2] = e3
            G[e2][e1] = e3
        floyd_warshall(G)
        res = collections.defaultdict(list)
        for k in G.keys():
            for kk in G[k].keys():
                if k == kk:
                    continue
                if G[k][kk] <= distanceThreshold:
                    res[k].append(kk)
        for i in range(n - 1, -1, -1):
            if i not in res:
                return i
        res = tuple((k, len(v)) for k, v in res.items())
        return sorted(res, key=lambda x: (x[1], -x[0]))[0][0]


so = Solution()
print(so.findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4))
print(
    so.findTheCity(n=5, edges=[[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], distanceThreshold=2))
print(so.findTheCity(6,
                     [[0, 3, 7], [2, 4, 1], [0, 1, 5], [2, 3, 10], [1, 3, 6], [1, 2, 1]],
                     417))

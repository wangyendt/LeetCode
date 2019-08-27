# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/8/27 17:06
# software: PyCharm


class Solution:
    def canFinish(self, n: int, prerequisites: list(list())) -> bool:
        G = [[] for _ in range(n)]
        degree = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n


so = Solution()
print(so.canFinish(2, [[0, 1]]))
print(so.canFinish(2, [[0, 1], [1, 0]]))
print(so.canFinish(5, [[0, 1], [0, 2]]))
print(so.canFinish(5, [[0, 1], [1, 2], [2, 0]]))

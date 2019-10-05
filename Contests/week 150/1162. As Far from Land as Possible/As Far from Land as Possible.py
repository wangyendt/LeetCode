#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: As Far from Land as Possible
@time: 2019/8/20 15:36
"""
import collections


class Solution:
    def maxDistance(self, grid: list(list())) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(q) == m * n or len(q) == 0: return -1
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xi, yj = x + i, y + j
                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        q.append((xi, yj))
                        grid[xi][yj] = 1
            level += 1
        return level - 1


so = Solution()
print(so.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))

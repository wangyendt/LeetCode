#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Path With Minimum Effort
@time: 2020/10/25 10:44
"""

from typing import *
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        inf = 10 ** 6 + 1
        m, n = len(heights), len(heights[0])
        res = [[inf for _ in range(n)] for _ in range(m)]
        priority_queue = [(0, 0, 0)]
        while priority_queue:
            d, i, j = heapq.heappop(priority_queue)
            if i == m - 1 and j == n - 1:
                return d
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nd = max(d, abs(heights[ni][nj] - heights[i][j]))
                    if res[ni][nj] > nd:
                        res[ni][nj] = nd
                        heapq.heappush(priority_queue, (res[ni][nj], ni, nj))
        return res[-1][-1]


so = Solution()
print(so.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(so.minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]))

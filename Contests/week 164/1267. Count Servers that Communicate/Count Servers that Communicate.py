#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count Servers that Communicate
@time: 2019/11/27 14:17
"""


class Solution:
    def countServers(self, grid: list(list())) -> int:
        R, C = len(grid), len(grid[0])
        ret = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    ret += any(grid[i][c] for i in range(R) if i != r) or any(grid[r][j] for j in range(C) if j != c)
        return ret


so = Solution()
print(so.countServers([[1, 0], [0, 1]]))
print(so.countServers([[1, 0], [1, 1]]))
print(so.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))

#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Path with Maximum Gold
@time: 2019/10/8 11:37
"""


class Solution:
    def getMaximumGold(self, grid: list(list())) -> int:
        M, N = len(grid), len(grid[0])

        def dfs(i, j, gold):
            if 0 <= i < M and 0 <= j < N and grid[i][j]:
                curr_gold, grid[i][j] = grid[i][j], 0
                gold = max(dfs(x, y, gold + curr_gold) for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)))
                grid[i][j] = curr_gold
            return gold

        return max(dfs(i, j, 0) for i in range(M) for j in range(N))


so = Solution()
print(so.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
print(so.getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))

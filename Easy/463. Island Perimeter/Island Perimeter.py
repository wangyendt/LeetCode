# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/12 16:08
# software: PyCharm

class Solution:
    def islandPerimeter(self, grid: list(list())) -> int:
        def helper(i, j, m, n):
            f = lambda x: min(max(x, 0), m - 1)
            g = lambda x: min(max(x, 0), n - 1)
            return {(f(i - 1), j), (f(i + 1), j), (i, g(j - 1)), (i, g(j + 1))} - {(i, j)}

        if not grid: return 0
        m, n = len(grid), len(grid[0])
        cnt1, cnt2 = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt1 += 1
                    for ii, jj in helper(i, j, m, n):
                        if grid[ii][jj] == 1:
                            cnt2 += 1
        return 4 * cnt1 - cnt2


so = Solution()
print(so.islandPerimeter([[0, 1, 0, 0],
                          [1, 1, 1, 0],
                          [0, 1, 0, 0],
                          [1, 1, 0, 0]]))

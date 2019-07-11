# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/11 11:10
# software: PyCharm

class Solution:
    def calculateMinimumHP(self, dungeon: list(list())) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if i == m - 1:
                    if j == n - 1:
                        dp[i][j] = max(1 - dungeon[i][j], 1)
                    else:
                        dp[i][j] = max(dp[i][j + 1] - dungeon[i][j], 1)
                else:
                    if j == n - 1:
                        dp[i][j] = max(dp[i + 1][j] - dungeon[i][j], 1)
                    else:
                        dp[i][j] = max(min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j], 1)
        return dp[0][0]


so = Solution()
print(so.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))

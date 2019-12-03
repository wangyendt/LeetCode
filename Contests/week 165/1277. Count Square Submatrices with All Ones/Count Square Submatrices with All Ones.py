#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count Square Submatrices with All Ones
@time: 2019/12/3 13:10
"""


class Solution:
    def countSquares(self, matrix: list(list())) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = matrix[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return sum(map(sum, dp))


so = Solution()
print(so.countSquares([
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]))

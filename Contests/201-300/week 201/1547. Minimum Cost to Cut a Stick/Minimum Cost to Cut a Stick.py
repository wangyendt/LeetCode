#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Cost to Cut a Stick
@time: 2020/08/10 00:18
"""


class Solution:
    def minCost(self, n: int, A: list) -> int:
        A = sorted(A + [0, n])
        k = len(A)
        dp = [[0] * k for _ in range(k)]
        for d in range(2, k):
            for i in range(k - d):
                dp[i][i + d] = min(dp[i][m] + dp[m][i + d] for m in range(i + 1, i + d)) + A[i + d] - A[i]
        return dp[0][k - 1]

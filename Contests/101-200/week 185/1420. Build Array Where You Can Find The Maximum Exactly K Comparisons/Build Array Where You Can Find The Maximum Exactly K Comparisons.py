#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/19 22:43
@Author:  wang121ye
@File: Build Array Where You Can Find The Maximum Exactly K Comparisons.py
@Software: PyCharm
"""

import itertools


class Solution:
    def numOfArrays(self, N: int, M: int, K: int) -> int:
        dp = [[[0 for _ in range(M + 1)] for _ in range(K + 1)] for _ in range(N + 1)]
        # the array has length of 1, and 1 jump, only 1 way to do that, for any k
        for k in range(1, M + 1):
            dp[1][1][k] = 1

        for i, j, k in itertools.product(range(1, N + 1), range(1, K + 1), range(M + 1)):
            dp[i][j][k] += dp[i - 1][j][k] * k
            dp[i][j][k] += sum(dp[i - 1][j - 1][1:k])

        return sum(dp[N][K][1:]) % (10 ** 9 + 7)

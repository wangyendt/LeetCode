#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/18 23:45
@Author:  wang121ye
@File: Restore The Array.py
@Software: PyCharm
"""

import math


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        s = [*map(int, s)] + [math.inf]  # for easier implementation
        dp = [0] * n + [1]
        for i in range(n - 1, -1, -1):
            num, j = s[i], i + 1
            while 1 <= num <= k and j < n + 1:
                dp[i] = (dp[i] + dp[j]) % 1000000007
                num = 10 * num + s[j]
                j += 1
        return dp[0]

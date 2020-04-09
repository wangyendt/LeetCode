#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Stone Game III
@time: 2020/4/9 15:28
"""


class Solution:
    def stoneGameIII(self, A):
        def cmp(x):
            if x > 0:
                return 1
            elif x < 0:
                return 2
            return 0

        dp = [0] * 3
        for i in range(len(A) - 1, -1, -1):
            dp[i % 3] = max(sum(A[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        return ["Tie", "Alice", "Bob"][cmp(dp[0])]


so = Solution()
print(so.stoneGameIII(A=[1, 2, 3, 7]))
print(so.stoneGameIII(A=[1, 2, 3, -9]))
print(so.stoneGameIII(A=[1, 2, 3, 6]))

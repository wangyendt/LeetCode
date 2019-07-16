# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/16 14:16
# software: PyCharm

class Solution:
    def fib(self, N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1
        dp = [0] * (N + 1)
        dp[1] = 1
        for i in range(2, N + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[-1]


so = Solution()
print(so.fib(3))

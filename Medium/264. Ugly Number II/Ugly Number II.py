#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Ugly Number II
@time: 2020/07/03 03:21
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        f2, f3, f5 = 0, 0, 0
        dp = [1] + [0] * (n - 1)
        for i in range(1, n):
            n2, n3, n5 = 2 * dp[f2], 3 * dp[f3], 5 * dp[f5]
            n_min = min(n2, n3, n5)
            if n_min == n2:
                f2 += 1
            if n_min == n3:
                f3 += 1
            if n_min == n5:
                f5 += 1
            dp[i] = n_min
            # print(i, f2, f3, f5, n2, n3, n5, n_min, dp)
        return dp[-1]


so = Solution()
print(so.nthUglyNumber(10))

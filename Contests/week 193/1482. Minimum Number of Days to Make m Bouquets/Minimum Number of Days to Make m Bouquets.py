#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Number of Days to Make m Bouquets
@time: 2020/06/14 10:40
"""

import sys
import functools


class Solution:
    def minDays(self, bloomDay: list, m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        inf = sys.maxsize
        n = len(bloomDay)
        dp = [[inf for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j < (i + 1) * k - 1:
                    continue
                elif j == (i + 1) * k - 1:
                    dp[i][j] = max(bloomDay[:j + 1])
                else:
                    dp[i][j] = min(
                        dp[i][j - 1], max(0 if i == 0 else dp[i - 1][j - k], max(bloomDay[j - k + 1:j + 1]))
                    )
        return dp[-1][-1] if dp[-1][-1] != inf else -1

    def minDays2(self, A, m, k):
        if m * k > len(A): return -1
        left, right = 1, max(A)
        while left < right:
            mid = (left + right) // 2
            flow = bouq = 0
            for a in A:
                flow = 0 if a > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left


so = Solution()
print(so.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
print(so.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2))
print(so.minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))
print(so.minDays(bloomDay=[1000000000, 1000000000], m=1, k=1))
print(so.minDays(bloomDay=[1, 10, 2, 9, 3, 8, 4, 7, 5, 6], m=4, k=2))

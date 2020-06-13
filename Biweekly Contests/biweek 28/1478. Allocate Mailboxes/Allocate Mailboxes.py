#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Allocate Mailboxes
@time: 2020/06/13 23:33
"""

import functools
import sys


class Solution:
    def minDistance(self, houses: list, k: int) -> int:
        def dist(start: int, end: int):
            total = 0
            while start < end:
                total += houses[end] - houses[start]
                start += 1
                end -= 1
            return total

        @functools.lru_cache(None)
        def dfs(i: int, last: int, group: int) -> int:
            if i == n: return sys.maxsize
            if group == k - 1: return dist(i, n - 1)
            new_group = dfs(i + 1, i + 1, group + 1) + dist(last, i)
            no_new_group = dfs(i + 1, last, group)
            return min(new_group, no_new_group)

        n = len(houses)
        houses.sort()
        return dfs(0, 0, 0)

    def minDistance2(self, A, k):
        A.sort()
        n = len(A)
        B = [0]
        for i, a in enumerate(A):
            B.append(B[i] + a)

        def cal(i, j):
            m1, m2 = (i + j) // 2, (i + j + 1) // 2
            med = (A[m1] + A[m2]) / 2.0
            return (B[j + 1] - B[m2]) - (B[m1 + 1] - B[i])

        dp = [cal(0, j) for j in range(n)]
        for k in range(2, k + 1):
            for j in range(n - 1, k - 2, -1):
                for i in range(k - 2, j):
                    dp[j] = min(dp[j], dp[i] + cal(i + 1, j))
        return int(dp[-1])


so = Solution()
print(so.minDistance(houses=[1, 4, 8, 10, 20], k=3))
print(so.minDistance(houses=[2, 3, 5, 12, 18], k=2))
print(so.minDistance(houses=[7, 4, 6, 1], k=1))
print(so.minDistance(houses=[3, 6, 14, 10], k=4))
print(so.minDistance2(A=[1, 4, 8, 10, 20], k=3))
print(so.minDistance2(A=[2, 3, 5, 12, 18], k=2))
print(so.minDistance2(A=[7, 4, 6, 1], k=1))
print(so.minDistance2(A=[3, 6, 14, 10], k=4))

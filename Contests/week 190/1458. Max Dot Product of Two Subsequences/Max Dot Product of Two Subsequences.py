#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/24 11:07
@Author:  wang121ye
@File: Max Dot Product of Two Subsequences.py
@Software: PyCharm
"""


class Solution:
    def maxDotProduct(self, nums1: list, nums2: list) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = nums1[i] * nums2[j]
                if i and j:
                    dp[i][j] += max(dp[i - 1][j - 1], 0)
                if i:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j])
                if j:
                    dp[i][j] = max(dp[i][j - 1], dp[i][j])
        return dp[-1][-1]


so = Solution()
print(so.maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]))
print(so.maxDotProduct(nums1=[3, -2], nums2=[2, -6, 7]))
print(so.maxDotProduct(nums1=[-1, -1], nums2=[1, 1]))

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Project -> File   ：LeetCode -> Minimum Number of Taps to Open to Water a Garden
@IDE    ：PyCharm
@Author ：Wang Ye (Wayne)
@Date   ：2020/1/27 13:34
@Desc   ：
=================================================="""


class Solution:
    def minTaps(self, n: int, ranges: list) -> int:
        dp = [0] + [n + 2] * n
        for i, r in enumerate(ranges):
            for j in range(max(i - r, 0), min(i + r, n) + 1):
                dp[j] = min(dp[j], dp[max(i - r, 0)] + 1)
        return dp[-1] if dp[-1] < n + 2 else -1


so = Solution()
print(so.minTaps(n=5, ranges=[3, 4, 1, 1, 0, 0]))
print(so.minTaps(n=3, ranges=[0, 0, 0, 0]))
print(so.minTaps(n=7, ranges=[1, 2, 1, 0, 2, 1, 0, 1]))
print(so.minTaps(n=8, ranges=[4, 0, 0, 0, 0, 0, 0, 0, 4]))
print(so.minTaps(n=8, ranges=[4, 0, 0, 0, 4, 0, 0, 0, 4]))

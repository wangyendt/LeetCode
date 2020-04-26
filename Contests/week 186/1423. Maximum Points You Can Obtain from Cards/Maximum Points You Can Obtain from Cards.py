#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/26 19:49
@Author:  wang121ye
@File: Maximum Points You Can Obtain from Cards.py
@Software: PyCharm
"""


class Solution:
    def maxScore(self, cardPoints: list, k: int) -> int:
        dp = [0 for _ in range(k+1)]
        dp[0] = sum(cardPoints[-k:])
        for i in range(1, k+1):
            dp[i] = dp[i-1] + cardPoints[i-1] - cardPoints[-k+i-1]
        return max(dp)

so = Solution()
# print(so.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
# print(so.maxScore(cardPoints=[2, 2, 2], k=2))
# print(so.maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7))
# print(so.maxScore(cardPoints=[1, 1000, 1], k=1))
# print(so.maxScore(cardPoints=[1, 79, 80, 1, 1, 1, 200, 1], k=3))
print(so.maxScore([96, 90, 41, 82, 39, 74, 64, 50, 30], 8))

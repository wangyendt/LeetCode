#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/17 17:25
@Author:  wang121ye
@File: Form Largest Integer With Digits That Add up to Target.py
@Software: PyCharm
"""


class Solution:
    def largestNumber(self, cost: list, target: int) -> str:
        dp = [0] + [-1] * (target + 5000)
        for t in range(1, target + 1):
            dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
        return str(max(dp[t], 0))

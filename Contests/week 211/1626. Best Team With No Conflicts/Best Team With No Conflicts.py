#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Best Team With No Conflicts
@time: 2020/10/19 00:19
"""

from typing import *


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        z = sorted(zip(ages, scores))
        n = len(z)
        dp = [0] * n
        for i in range(n):
            dp[i] = z[i][1]
            for j in range(i):
                if z[j][1] <= z[i][1]:
                    dp[i] = max(dp[i], dp[j] + z[i][1])

        return max(dp)

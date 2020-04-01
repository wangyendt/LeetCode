#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Count Number of Teams.py 
@time: 2020/04/01
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def numTeams(self, rating: list) -> int:
        n = len(rating)
        dp = [[0, 0, 0] for _ in range(n)]
        for i, r in enumerate(rating):
            if i > 0: dp[i][2] = dp[i - 1][2]
            for j in range(i):
                if rating[j] < rating[i]:
                    dp[i][2] += dp[j][0]
                    dp[i][0] += 1
                if rating[j] > rating[i]:
                    dp[i][2] += dp[j][1]
                    dp[i][1] += 1
        # print(dp)
        return dp[-1][2]


so = Solution()
print(so.numTeams(rating=[2, 5, 3, 4, 1]))
print(so.numTeams(rating=[2, 1, 3]))
print(so.numTeams(rating=[1, 2, 3, 4]))

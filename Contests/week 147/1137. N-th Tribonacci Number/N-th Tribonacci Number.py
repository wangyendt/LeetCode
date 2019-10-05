#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: N-th Tribonacci Number.py 
@time: 2019/07/28
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[-1]


so = Solution()
print(so.tribonacci(0))
print(so.tribonacci(4))
print(so.tribonacci(25))
print(so.tribonacci(37))

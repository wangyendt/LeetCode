#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Ways To Build Good Strings.py 
@time: 2022/11/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        mod = 10 ** 9 + 7
        for i in range(1, high + 1):
            if i == zero:
                dp[i] += 1
            if i == one:
                dp[i] += 1
            if i > zero:
                # print(i, len(dp))
                dp[i] = (dp[i] + dp[i - zero]) % mod
            if i > one:
                dp[i] = (dp[i] + dp[i - one]) % mod
        return sum(dp[i] for i in range(low, high + 1)) % mod


so = Solution()
print(so.countGoodStrings(low=3, high=3, zero=1, one=1))

#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Perfect Squares.py 
@time: 2019/12/21
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        for i in range(1, n + 1):
            if i == int(i ** 0.5) ** 2:
                dp[i] = 1
            else:
                for j in range(1, int(i ** 0.5) + 1):
                    dp[i] = min(dp[i], dp[i - j ** 2] + 1)
        return dp[-1]


so = Solution()
print(so.numSquares(12))
print(so.numSquares(13))

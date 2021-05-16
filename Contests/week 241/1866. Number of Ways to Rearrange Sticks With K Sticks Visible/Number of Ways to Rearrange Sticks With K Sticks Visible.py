#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Ways to Rearrange Sticks With K Sticks Visible.py 
@time: 2021/05/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import math


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[1][1] = 1
        if n > 1:
            dp[2][1] = 1
        if k > 1:
            dp[2][2] = 1
        for i in range(2, n + 1):
            for j in range(1, min(i, k) + 1):
                # print(i, j)
                if j == i:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] * (i - 1) + dp[i - 1][j - 1]
        # [print(d) for d in dp]
        return dp[n][k] % (10 ** 9 + 7)


so = Solution()
print(so.rearrangeSticks(n=3, k=2))
print(so.rearrangeSticks(n=5, k=5))
print(so.rearrangeSticks(n=20, k=11))

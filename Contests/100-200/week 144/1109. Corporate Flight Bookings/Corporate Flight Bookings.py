#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Corporate Flight Bookings.py 
@time: 2019/07/07
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

from collections import defaultdict


class Solution:
    def corpFlightBookings(self, bookings: list(list()), n: int) -> list:
        dp = [0] * (n + 1)
        for i, j, k in bookings:
            dp[i - 1] += k
            dp[j] -= k
        for i in range(1, n):
            dp[i] += dp[i - 1]
        return dp[:-1]


so = Solution()
print(so.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
print(so.corpFlightBookings([[2, 2, 30], [2, 2, 45]], 2))

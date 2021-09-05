#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: First Day Where You Have Been in All the Rooms.py 
@time: 2021/09/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n
        A = [0]
        MOD = 10 ** 9 + 7

        def get_sum(i, j):
            return A[j + 1] - A[i]

        for i in range(n):
            if i == nextVisit[i]:
                dp[i] = 1
            else:
                dp[i] = get_sum(nextVisit[i], i - 1) + (i - nextVisit[i] + 1)
                dp[i] %= MOD
            A.append(A[-1] + dp[i])
        # print(dp)
        dp2 = [1] * n
        for i in range(1, n):
            dp2[i] = dp2[i - 1] + dp[i - 1] + 1
            dp2[i] %= MOD
        # print(dp2)
        return (dp2[-1] - 1) % MOD


so = Solution()
print(so.firstDayBeenInAllRooms([0, 0]))
print(so.firstDayBeenInAllRooms(nextVisit=[0, 0, 2]))
print(so.firstDayBeenInAllRooms(nextVisit=[0, 1, 2, 0]))
print(so.firstDayBeenInAllRooms(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

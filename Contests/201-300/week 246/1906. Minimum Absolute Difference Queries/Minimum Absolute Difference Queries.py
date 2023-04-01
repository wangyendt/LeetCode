#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Absolute Difference Queries.py 
@time: 2021/06/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools
import sys
# sys.setrecursionlimit(100000)
import collections


class Solution:
    def minDifference(self, A: List[int], Q: List[List[int]]) -> List[int]:
        N, ans, dp = max(A), [], [[0] * (max(A) + 1)]

        for num in A:
            t = dp[-1][:]
            t[num] += 1
            dp.append(t)

        for a, b in Q:
            diff = [i for x, y, i in zip(dp[b + 1], dp[a], range(N + 1)) if y != x]
            ans.append(min([b - a for a, b in zip(diff, diff[1:])] or [-1]))

        return ans


so = Solution()
print(so.minDifference([4, 5, 2, 2, 7, 10], [[2, 3], [0, 2], [0, 5], [3, 5]]))

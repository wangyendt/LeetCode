#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Score from Performing Multiplication Operations.py 
@time: 2021/02/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools
import sys

sys.setrecursionlimit(1000000)


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        @functools.lru_cache(None)
        def dp(i, j):
            if j == m:
                return 0
            left = dp(i + 1, j + 1) + nums[i] * multipliers[j]
            right = dp(i, j + 1) + nums[n - 1 - (j - i)] * multipliers[j]
            return max(left, right)

        return dp(0, 0)


so = Solution()
# print(so.maximumScore(nums=[1, 2, 3], multipliers=[3, 2, 1]))
# print(so.maximumScore(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]))
# print(so.maximumScore(
#     [555, 526, 732, 182, 43, -537, -434, -233, -947, 968, -250, -10, 470, -867, -809, -987, 120, 607, -700, 25, -349,
#      -657, 349, -75, -936, -473, 615, 691, -261, -517, -867, 527, 782, 939, -465, 12, 988, -78, -990, 504, -358, 491,
#      805, 756, -218, 513, -928, 579, 678, 10],
#     [783, 911, 820, 37, 466, -251, 286, -74, -899, 586, 792, -643, -969, -267, 121, -656, 381, 871, 762, -355, 721, 753,
#      -521]
# ))
print(so.maximumScore(list(range(100000)), list(range(1000))))

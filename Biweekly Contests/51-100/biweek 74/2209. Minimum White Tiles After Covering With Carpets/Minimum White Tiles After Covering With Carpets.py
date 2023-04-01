#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum White Tiles After Covering With Carpets.py 
@time: 2022/03/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
import heapq

import functools


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        @functools.lru_cache(None)
        def dp(i, k):
            if i <= 0: return 0
            return min(int(floor[i - 1]) + dp(i - 1, k), dp(i - carpetLen, k - 1) if k else 1000)

        return dp(len(floor), numCarpets)


so = Solution()
print(so.minimumWhiteTiles(floor="10110101", numCarpets=2, carpetLen=2))
print(so.minimumWhiteTiles(floor="11111", numCarpets=2, carpetLen=3))
print(so.minimumWhiteTiles("111111111111", 9, 1))

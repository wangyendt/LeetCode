#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: House Robber IV.py 
@time: 2023/02/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)
        while l < r:
            m = (l + r) // 2
            last = take = 0
            for a in nums:
                if last:
                    last = 0
                    continue
                if a <= m:
                    take += 1
                    last = 1
            if take >= k:
                r = m
            else:
                l = m + 1
        return l


so = Solution()
print(so.minCapability(nums=[2, 3, 5, 9], k=2))
print(so.minCapability(nums=[2, 7, 9, 3, 1], k=2))
print(so.minCapability([1], 1))
print(so.minCapability([9, 6, 20, 21, 8], 3))
print(so.minCapability([35, 9, 18, 78, 40, 8, 71, 2, 59], 5))

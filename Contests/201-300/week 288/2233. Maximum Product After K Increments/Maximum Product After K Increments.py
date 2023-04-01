#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Product After K Increments.py 
@time: 2022/04/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq
import functools


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k > 0:
            heapq.heappush(nums, heapq.heappop(nums) + 1)
            k -= 1
        mod = 10 ** 9 + 7
        return functools.reduce(lambda x, y: (x * y) % mod, nums)


so = Solution()
print(so.maximumProduct(nums=[0, 4], k=5))

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Operations to Halve Array Sum.py 
@time: 2022/03/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        s_raw = s = -sum(nums)
        ret = 0
        while s > s_raw / 2:
            num = -heapq.heappop(nums)
            s -= num / 2
            heapq.heappush(nums, -num / 2)
            ret += 1
            # print(s, s_raw, nums)
        return ret


so = Solution()
print(so.halveArray(nums=[5, 19, 8, 1]))

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find the Middle Index in Array.py 
@time: 2021/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # if sum(nums) == 0: return 0
        for i in range(len(nums)):
            # print(sum(nums[:i]))
            # print(sum(nums[i + 1:]))
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


so = Solution()
print(so.findMiddleIndex([-2, 4, -3, 1, 0]))
print(so.findMiddleIndex([1, -1, 1]))

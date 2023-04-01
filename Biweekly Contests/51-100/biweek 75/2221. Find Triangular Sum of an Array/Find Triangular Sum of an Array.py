#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Triangular Sum of an Array.py 
@time: 2022/04/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        while True:
            for i, n in enumerate(nums):
                if i < len(nums) - 1:
                    nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()
            if len(nums) == 1:
                return nums[0]


so = Solution()
print(so.triangularSum([1, 2, 3, 4, 5]))

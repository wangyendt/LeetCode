#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Swaps to Group All 1's Together II.py 
@time: 2022/01/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        nums = nums + nums
        x, onesInWindow = 0, 0
        for i in range(len(nums)):
            if i >= ones and nums[i - ones]: x -= 1
            if nums[i] == 1: x += 1
            onesInWindow = max(x, onesInWindow)
        return ones - onesInWindow

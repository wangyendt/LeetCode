#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimize the Maximum Difference of Pairs.py 
@time: 2023/04/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def can_form_pairs(nums, max_diff, p):
            pairs_count = 0
            i = 0
            while i < len(nums) - 1 and pairs_count < p:
                if nums[i + 1] - nums[i] <= max_diff:
                    pairs_count += 1
                    i += 2
                else:
                    i += 1
            return pairs_count >= p

        nums.sort()

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = left + (right - left) // 2

            if can_form_pairs(nums, mid, p):
                right = mid
            else:
                left = mid + 1

        return left

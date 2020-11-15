#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Distribute Repeating Integers.py 
@time: 2020/11/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from collections import Counter
import bisect
from typing import *


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        nums = list(Counter(nums).values())
        nums.sort()

        quantity.sort(reverse=True)

        def solve(qi):
            if qi == len(quantity):
                return True
            elif len(nums) == 0:
                return False
            else:
                cs = bisect.bisect_left(nums, quantity[qi])
                if cs < len(nums) and nums[cs] >= quantity[qi]:
                    for x in range(cs, len(nums)):
                        r = nums.pop(x)
                        rem = r - quantity[qi]
                        idx = bisect.bisect_right(nums, rem)
                        bisect.insort(nums, rem)
                        if solve(qi + 1):
                            return True
                        del nums[idx]
                        nums.insert(idx, r)

                return False

        return solve(0)

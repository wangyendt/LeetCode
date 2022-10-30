#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Operations to Make Arrays Similar.py 
@time: 2022/10/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort(key=lambda a: (a & 1, a))
        target.sort(key=lambda a: (a & 1, a))
        # print(nums, target)
        return sum(abs(a - b) for a, b in zip(nums, target)) // 4


so = Solution()
print(so.makeSimilar(nums=[8, 12, 6], target=[2, 14, 10]))
print(so.makeSimilar(nums=[1, 2, 5], target=[4, 1, 3]))

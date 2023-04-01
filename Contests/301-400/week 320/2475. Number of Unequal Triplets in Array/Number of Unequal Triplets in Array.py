#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Unequal Triplets in Array.py 
@time: 2022/11/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
from math import comb


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if i < j < k and nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        ret += 1
        return ret


so = Solution()
print(so.unequalTriplets(nums=[4, 4, 2, 4, 3]))

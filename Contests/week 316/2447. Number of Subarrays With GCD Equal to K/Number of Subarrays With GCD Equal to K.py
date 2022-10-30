#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Subarrays With GCD Equal to K.py 
@time: 2022/10/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
from math import gcd
import functools


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ret = 0
        for left in range(len(nums)):
            cur = nums[left]
            for right in range(left, len(nums)):
                cur = gcd(cur, nums[right])
                if cur == k:
                    ret += 1
        return ret


so = Solution()
print(so.subarrayGCD(nums=[9, 3, 1, 2, 6, 3], k=3))

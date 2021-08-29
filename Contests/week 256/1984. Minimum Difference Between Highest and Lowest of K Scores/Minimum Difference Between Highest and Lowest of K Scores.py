#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Difference Between Highest and Lowest of K Scores.py 
@time: 2021/08/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1: return 0
        nums.sort()
        n = len(nums)
        ret = float('inf')
        for i in range(n):
            if i + k - 1 >= n: break
            sub = nums[i + k - 1] - nums[i]
            ret = min(ret, sub)
        return ret

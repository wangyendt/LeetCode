#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Subarrays With Equal Sum.py 
@time: 2022/09/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        res = collections.defaultdict(int)
        for i, n in enumerate(nums):
            if i < len(nums) - 1:
                s = nums[i] + nums[i + 1]
                res[s] += 1
                if res[s] >= 2:
                    return True
        return False

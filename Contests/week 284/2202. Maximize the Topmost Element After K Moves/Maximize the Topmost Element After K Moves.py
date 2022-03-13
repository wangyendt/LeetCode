#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximize the Topmost Element After K Moves.py 
@time: 2022/03/13
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0: return nums[0]
        nums = nums[:k + 1]
        if len(nums) == 1 and k & 1:
            return -1
        if k == 1:
            if len(nums) == 1:
                return -1
            else:
                return nums[1]
        ret = max(nums[:k - 1])
        if k <= len(nums) - 1:
            ret = max(ret, nums[k])
        return ret

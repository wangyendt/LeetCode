#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check if Array Is Sorted and Rotated.py 
@time: 2021/02/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                cnt += 1
                if cnt >= 2 or nums[-1] > nums[0]:
                    return False
        return True

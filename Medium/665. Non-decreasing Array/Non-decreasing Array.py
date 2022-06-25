#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Non-decreasing Array.py 
@time: 2022/06/25
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        idx = 0
        for i, n in enumerate(nums):
            if i and n < nums[i - 1]:
                idx = i
                cnt += 1
                if cnt > 1: return False
        if cnt == 1:
            # print(nums, nums[:idx - 1] + nums[idx:], nums[:idx] + nums[idx + 1:])
            if not (nums[:idx - 1] + nums[idx:] == sorted(nums[:idx - 1] + nums[idx:]) or
                    nums[:idx] + nums[idx + 1:] == sorted(nums[:idx] + nums[idx + 1:])):
                return False
        return True


so = Solution()
print(so.checkPossibility([4, 2, 3]))
print(so.checkPossibility([4, 2, 1]))
print(so.checkPossibility([3, 4, 2, 3]))

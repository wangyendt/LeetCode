#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Remove One Element to Make the Array Strictly Increasing.py 
@time: 2021/06/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                break
        else:
            return True
        A = nums[:i] + nums[i + 1:]
        B = nums[:i + 1] + nums[i + 2:]
        # print(A, B)
        for i, a in enumerate(A):
            if i > 0 and a <= A[i - 1]:
                break
        else:
            return True
        for i, b in enumerate(B):
            if i > 0 and b <= B[i - 1]:
                break
        else:
            return True
        return False


so = Solution()
print(so.canBeIncreasing(nums=[1, 2, 10, 5, 7]))
print(so.canBeIncreasing([1, 2, 3]))

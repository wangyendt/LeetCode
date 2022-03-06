#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Append K Integers With Minimal Sum.py 
@time: 2022/03/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)

        if nums[n - 1] <= k + n:
            return (k + n) * (k + n + 1) // 2 - sum(nums)

        lft, rgt = 0, n - 1
        while rgt > lft:
            mid = (lft + rgt) // 2
            if nums[mid] - mid <= k:
                lft = mid + 1
            else:
                rgt = mid

        return (k + lft) * (k + lft + 1) // 2 - sum(nums[:lft])


so = Solution()
print(so.minimalKSum(nums=[1, 4, 25, 10, 25], k=2))
print(so.minimalKSum(nums=[5, 6], k=6))
print(so.minimalKSum([53, 41, 90, 33, 84, 26, 50, 32, 63, 47, 66, 43, 29, 88, 71, 28, 83], 76))
print(so.minimalKSum(nums=[5, 68756767], k=66546646))

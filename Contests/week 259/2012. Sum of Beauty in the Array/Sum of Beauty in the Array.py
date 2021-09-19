#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Beauty in the Array.py 
@time: 2021/09/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        mx, mn = [0] * n, [float('inf')] * n
        for i, num in enumerate(nums):
            if i == 0:
                mx[i] = num
                continue
            mx[i] = max(mx[i - 1], num)
        for i in range(len(nums))[::-1]:
            if i == n - 1:
                mn[i] = nums[i]
            else:
                mn[i] = min(mn[i + 1], nums[i])
        # print(f'{nums=},{mx=},{mn=}')
        ret = 0
        for i in range(1, n - 1):
            if mn[i + 1] > nums[i] > mx[i - 1]:
                ret += 2
            elif nums[i + 1] > nums[i] > nums[i - 1]:
                ret += 1
            else:
                ret += 0
        return ret


so = Solution()
print(so.sumOfBeauties([1, 2, 3]))
print(so.sumOfBeauties([2, 4, 6, 4]))
print(so.sumOfBeauties(nums=[3, 2, 1]))

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Average Difference.py 
@time: 2022/04/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import sys


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = sys.maxsize
        ret = 0
        p = 0
        l = 0
        r = sum(nums)
        n = len(nums)
        while p < n:
            l += nums[p]
            r -= nums[p]
            l_avg = l // (p + 1)
            r_avg = (r // (n - 1 - p)) if p < n - 1 else 0
            cur = abs(l_avg - r_avg)
            # print(f'{p=},{l=},{r=},{cur=},{p+1=},{n-1-p=}')
            if cur < res:
                res = cur
                ret = p
            p += 1
        return ret


so = Solution()
print(so.minimumAverageDifference(nums=[2, 5, 3, 9, 5, 3]))
print(so.minimumAverageDifference([4, 2, 0]))

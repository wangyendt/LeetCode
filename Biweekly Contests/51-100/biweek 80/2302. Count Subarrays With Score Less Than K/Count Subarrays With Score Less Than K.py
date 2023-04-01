#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Subarrays With Score Less Than K.py 
@time: 2022/06/11
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l, r, s = 0, 0, 0
        ret = 0
        while r < N:
            s += nums[r]
            while l <= r:
                if (r - l + 1) * s >= k:
                    s -= nums[l]
                    l += 1
                else:
                    break
            else:
                r += 1
                continue
            ret += r - l + 1
            r += 1
        return ret


so = Solution()
print(so.countSubarrays(nums=[2, 1, 4, 3, 5], k=10))

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Special Quadruplets.py 
@time: 2021/09/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            ret += 1
        return ret


so = Solution()
print(so.countQuadruplets([28, 8, 49, 85, 37, 90, 20, 8]))

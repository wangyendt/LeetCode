#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Number of Maximum Bitwise-OR Subsets.py
@time: 2021/10/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        cnter = collections.defaultdict(int)
        for i in range(1 << n):
            res = 0
            for j in range(n):
                if (1 << j) & i:
                    res |= nums[j]
            cnter[res] += 1
        return max(cnter.items(), key=lambda x: x[0])[1]


so = Solution()
print(so.countMaxOrSubsets([3, 1]))

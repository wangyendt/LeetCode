#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Tuple with Same Product.py 
@time: 2021/01/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                res.append(nums[i] * nums[j])
        res = collections.Counter(res)
        # print(res)
        ret = 0
        for k, v in res.items():
            if v >= 2:
                ret += v * (v - 1) // 2
        return ret * 8


so = Solution()
print(so.tupleSameProduct([2, 3, 4, 6]))

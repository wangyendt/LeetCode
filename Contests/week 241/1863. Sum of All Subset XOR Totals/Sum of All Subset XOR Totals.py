#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of All Subset XOR Totals.py 
@time: 2021/05/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
from itertools import chain, combinations


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)

        def powerset(iterable):
            xs = list(iterable)
            return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))

        for tp in powerset(nums):
            res = 0
            for t in tp:
                res ^= t
            ret += res
        return ret


so = Solution()
print(so.subsetXORSum([1, 2, 3]))

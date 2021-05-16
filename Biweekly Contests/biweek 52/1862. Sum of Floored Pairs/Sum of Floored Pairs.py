#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Floored Pairs.py 
@time: 2021/05/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import itertools


class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        incs, counter = [0] * (max(nums) + 1), collections.Counter(nums)
        for num in counter:
            for j in range(num, len(incs), num):
                incs[j] += counter[num]
        quots = list(itertools.accumulate(incs))
        return sum([quots[num] for num in nums]) % (10 ** 9 + 7)

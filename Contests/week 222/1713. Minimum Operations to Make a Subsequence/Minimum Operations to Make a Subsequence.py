#!/usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Operations to Make a Subsequence.py 
@time: 2021/01/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        dic = {num: i for i, num in enumerate(target)}
        A = []
        for num in arr:
            if num in dic:
                A.append(dic[num])
        return len(target) - self.lengthOfLIS(A)

    def lengthOfLIS(self, nums):
        if not nums: return 0
        piles = []
        for num in nums:
            index = bisect.bisect_left(piles, num)
            if index == len(piles):
                piles.append(num)
            else:
                piles[index] = num
        return len(piles)

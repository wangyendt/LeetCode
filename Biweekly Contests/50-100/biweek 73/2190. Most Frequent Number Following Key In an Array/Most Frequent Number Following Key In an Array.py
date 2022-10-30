#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Most Frequent Number Following Key In an Array.py 
@time: 2022/03/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n = len(nums)
        cnt = collections.defaultdict(int)
        for i in range(n - 1):
            if nums[i] == key:
                cnt[nums[i + 1]] += 1
        return sorted(cnt.items(), key=lambda x: x[1])[-1][0]

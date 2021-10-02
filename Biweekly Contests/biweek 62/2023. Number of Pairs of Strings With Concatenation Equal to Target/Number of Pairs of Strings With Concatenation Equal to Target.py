# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Number of Pairs of Strings With Concatenation Equal to Target.py
@time: 2021/10/03
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import collections
import functools
import itertools


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ret = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    ret += 1
        return ret

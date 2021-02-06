#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Sum of Unique Elements
@time: 2021/02/06 22:30
"""

import collections
from typing import *


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnter = collections.Counter(nums)
        ret = 0
        for k, v in cnter.items():
            if v == 1:
                ret += k
        return ret


so = Solution()
print(so.sumOfUnique(nums=[1, 2, 3, 2]))

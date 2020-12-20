#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Erasure Value
@time: 2020/12/20 10:40
"""

from typing import *
import collections


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        stack = []
        ret = 0
        val = 0
        cur = collections.defaultdict(int)
        for n in nums:
            while cur[n] > 0:
                s = stack.pop(0)
                cur[s] -= 1
                val -= s
            stack.append(n)
            cur[n] += 1
            val += n
            ret = max(ret, val)
        return ret

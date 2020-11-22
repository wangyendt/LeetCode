#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Ways to Make a Fair Array
@time: 2020/11/22 10:50
"""

from typing import *


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        presum_odd_left = [0]
        presum_odd_right = [0]
        presum_even_left = [0]
        presum_even_right = [0]
        for i in range(0, n, 2):
            presum_odd_left.append(presum_odd_left[-1] + nums[i])
        for i in range(1, n, 2):
            presum_even_left.append(presum_even_left[-1] + nums[i])
        for i in range(n - 1, -1, -2):
            presum_odd_right.append(presum_odd_right[-1] + nums[i])
        for i in range(n - 2, -1, -2):
            presum_even_right.append(presum_even_right[-1] + nums[i])
        ret = 0
        if n % 2 == 0:
            for i in range(n):
                if presum_odd_left[(i + 1) // 2] + presum_odd_right[(n - i) // 2] == \
                        presum_even_left[i // 2] + presum_even_right[(n - 1 - i) // 2]:
                    ret += 1
        else:
            for i in range(n):
                if presum_odd_left[(i + 1) // 2] + presum_even_right[(n - 1 - i) // 2] == \
                        presum_even_left[i // 2] + presum_odd_right[(n - i) // 2]:
                    ret += 1
        return ret

#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Running Sum of 1d Array
@time: 2020/06/14 10:30
"""

import itertools


class Solution:
    def runningSum(self, nums: list) -> list:
        return list(itertools.accumulate(nums))

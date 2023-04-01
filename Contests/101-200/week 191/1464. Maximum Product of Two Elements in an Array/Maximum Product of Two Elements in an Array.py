#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Product of Two Elements in an Array
@time: 2020/05/31 10:32
"""


class Solution:
    def maxProduct(self, nums: list) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

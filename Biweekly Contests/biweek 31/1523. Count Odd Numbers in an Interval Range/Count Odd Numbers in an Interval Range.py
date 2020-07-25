#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count Odd Numbers in an Interval Range
@time: 2020/07/26 00:35
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0: low += 1
        if high % 2 == 0: high -= 1
        return (high - low) // 2 + 1

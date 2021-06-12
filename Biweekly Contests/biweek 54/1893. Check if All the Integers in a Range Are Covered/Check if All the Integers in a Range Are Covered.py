#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Check if All the Integers in a Range Are Covered
@time: 2021/06/13 00:07
"""

from typing import *


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        res = 0
        for n in range(left, right + 1):
            for r1, r2 in ranges:
                if r1 <= n <= r2:
                    res += 1
                    break
        if res == right - left + 1:
            return True
        return False

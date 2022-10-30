#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Keep Multiplying Found Values by Two
@time: 2022/02/01 00:54
"""

from typing import *


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        while original in num_set:
            original *= 2
        return original

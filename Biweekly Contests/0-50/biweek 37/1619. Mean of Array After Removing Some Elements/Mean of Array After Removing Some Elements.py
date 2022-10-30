#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Mean of Array After Removing Some Elements
@time: 2020/10/18 16:38
"""

from typing import *


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        sub = arr[n // 20:-n // 20]
        return sum(sub) / len(sub)

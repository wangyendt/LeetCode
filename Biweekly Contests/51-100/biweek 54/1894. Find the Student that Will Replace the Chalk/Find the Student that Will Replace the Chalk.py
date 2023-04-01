#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find the Student that Will Replace the Chalk
@time: 2021/06/13 00:15
"""

from typing import *


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        for i, c in enumerate(chalk):
            if k == 0:
                return i
            k -= chalk[i]
            if k < 0: return i

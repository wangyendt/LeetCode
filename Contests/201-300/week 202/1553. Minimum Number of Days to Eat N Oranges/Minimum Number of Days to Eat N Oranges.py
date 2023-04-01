#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Number of Days to Eat N Oranges
@time: 2020/08/17 01:13
"""

import functools


class Solution:
    @functools.lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))

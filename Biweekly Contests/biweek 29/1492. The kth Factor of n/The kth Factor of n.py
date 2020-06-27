#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: The kth Factor of n
@time: 2020/06/27 22:33
"""

import math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            if n % i == 0:
                cnt += 1
                if cnt == k: return i
        return -1

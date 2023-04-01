# !/usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@author: Wang Ye (Wayne)
@file: Convert 1D Array Into 2D Array.py
@time: 2021/10/02
@contact: wangye@oppo.com
@site: 
@software: PyCharm
# code is far away from bugs.
"""

from typing import *
import collections
import functools
import itertools


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        if l != m * n: return []
        ret = []
        for i in range(m):
            ret.append([])
            for j in range(n):
                idx = i * n + j
                ret[-1].append(original[idx])
        return ret

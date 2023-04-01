#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: wangye(Wayne)
@license: Apache Licence
@file: Minimum Consecutive Cards to Pick Up.py
@time: 2022/05/01
@contact: wang121ye@hotmail.com
@site:
@software: PyCharm

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = collections.defaultdict(list)
        for i, c in enumerate(cards):
            res[c].append(i)
        ret = 10 ** 9
        for k, v in res.items():
            if len(v) == 1:
                continue
            for i in range(len(v) - 1):
                ret = min(ret, v[i + 1] - v[i] + 1)
        if ret == 10 ** 9:  ret = -1
        return ret

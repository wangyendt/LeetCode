#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Search Suggestions System
@time: 2019/11/27 15:52
"""

import bisect


class Solution:
    def suggestedProducts(self, A: list, word: str) -> list(list()):
        A.sort()
        ret, prefix, i = [], '', 0
        for c in word:
            prefix += c
            i = bisect.bisect_left(A, prefix, i)
            ret.append([w for w in A[i:i + 3] if w.startswith(prefix)])
        return ret

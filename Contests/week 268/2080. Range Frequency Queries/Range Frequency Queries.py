#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Range Frequency Queries.py 
@time: 2021/11/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import bisect


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.A = collections.defaultdict(list)
        for i, a in enumerate(arr):
            self.A[a].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.A: return 0
        lo = bisect.bisect_left(self.A[value], left)
        hi = bisect.bisect_right(self.A[value], right)
        return hi - lo

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Query Kth Smallest Trimmed Number.py 
@time: 2022/07/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = collections.defaultdict(list)
        ret = []
        for q1, q2 in queries:
            t = [n[-q2:] for n in nums]
            if q2 not in res:
                res[q2] = sorted(range(len(nums)), key=lambda x: (t[x], x))
            ret.append(res[q2][q1 - 1])
        return ret

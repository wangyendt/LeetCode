#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Most Beautiful Item for Each Query.py 
@time: 2021/11/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import bisect


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        maxer = collections.defaultdict(int)
        items.sort()
        res = [item[0] for item in items]
        M = 0
        for p, b in items:
            M = max(M, b)
            maxer[p] = M
        ret = []
        for q in queries:
            idx = bisect.bisect_right(res, q)
            if idx == 0:
                ret.append(0)
            else:
                ret.append(maxer[res[max(0, idx - 1)]])
        return ret

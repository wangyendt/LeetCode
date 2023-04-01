#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Space Wasted From Packaging.py 
@time: 2021/06/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        presum = [0]
        packages.sort()
        for p in packages:
            presum.append(presum[-1] + p)

        def get_sum(i, j):
            return presum[j + 1] - presum[i]

        ret = 1e30
        for box in boxes:
            idx = 0
            box.sort()
            res = 0
            if box[-1] < packages[-1]:
                continue
            for b in box:
                idx2 = bisect.bisect_right(packages, b)
                if idx2 == 0:
                    continue
                res += (idx2 - idx) * b - get_sum(idx, idx2 - 1)
                idx = idx2
            ret = min(ret, res)
        if ret == 1e30:
            return -1
        return ret % (10 ** 9 + 7)

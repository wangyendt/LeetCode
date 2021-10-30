#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Plates Between Candles.py 
@time: 2021/10/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        cnt = 0
        n_cans = []
        start = False
        for i, t in enumerate(s):
            if t == '|':
                start = True
                res.append(i)
                n_cans.append(cnt)
                cnt = 0
            else:
                if start:
                    cnt += 1
        presum = [0]
        if not n_cans: return [0] * len(queries)
        for c in n_cans:
            presum.append(c + presum[-1])

        def get_n_cans(i, j):
            return presum[j + 1] - presum[i]

        ret = []
        for q1, q2 in queries:
            if q2 - q1 <= 1:
                ret.append(0)
            else:
                i1 = bisect.bisect_left(res, q1) + 1
                i2 = bisect.bisect_right(res, q2) - 1
                if i2 <= 0 or i1 > i2 or i1 >= len(res):
                    ret.append(0)
                else:
                    ret.append(get_n_cans(i1, i2))
        return ret


so = Solution()
print(so.platesBetweenCandles(s="|****|**********|", queries=[[0, 4], [0, 16]]))
print(so.platesBetweenCandles(s="|**|**|***|", queries=[[2, 5], [5, 10], [2, 9]]))
print(so.platesBetweenCandles(s="**|**|***|", queries=[[2, 5], [5, 9]]))
print(so.platesBetweenCandles(s="***|**|*****|**||**|*", queries=[[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
print(so.platesBetweenCandles("||||", queries=[[0, 1], [0, 3]]))
print(so.platesBetweenCandles("****", queries=[[0, 1], [0, 3]]))
print(so.platesBetweenCandles("|**|***|***|*", queries=[[0, 1], [0, 3], [0, 12]]))

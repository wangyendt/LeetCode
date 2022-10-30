#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Two Best Non-Overlapping Events.py 
@time: 2021/10/30
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        M = [0 for _ in range(n + 1)]
        res_e = []
        res_i = []
        ret = 0
        events.sort(key=lambda x: (x[1], x[0], x[2]))
        for i, (s, e, v) in enumerate(events):
            if i == 0:
                M[i + 1] = v
                ret = v
            else:
                idx = bisect.bisect_left(res_e, s)
                if idx == len(res_e):
                    ret = max(ret, v + M[i])
                else:
                    ret = max(ret, v + M[res_i[idx]])
                M[i + 1] = max(M[i], v)
            res_e.append(e)
            res_i.append(i)
        return ret


so = Solution()
print(so.maxTwoEvents(events=[[1, 3, 2], [4, 5, 2], [2, 4, 3]]))
print(so.maxTwoEvents(events=[[1, 3, 2], [4, 5, 2], [1, 5, 5]]))
print(so.maxTwoEvents(events=[[1, 5, 3], [1, 5, 1], [6, 6, 5]]))
print(so.maxTwoEvents([[10, 83, 53], [63, 87, 45], [97, 100, 32], [51, 61, 16]]))

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Time to Cross a Bridge.py 
@time: 2023/01/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        a, f, l, r, m, s = 0, 0, [], [], [], []
        for i in range(len(time)):
            heapq.heappush(m, (-time[i][0] - time[i][2], -i))
        while n or r or s:
            f = min(l[0][0] if n and l else float('inf'), r[0][0] if r else float('inf')) if not s and (not r or r[0][0] > f) and (not n or not m and (not l or l[0][0] > f)) else f
            while l and l[0][0] <= f:
                heapq.heappush(m, (-time[l[0][1]][0] - time[l[0][1]][2], -heapq.heappop(l)[1]))
            while r and r[0][0] <= f:
                heapq.heappush(s, (-time[r[0][1]][0] - time[r[0][1]][2], -heapq.heappop(r)[1]))
            if s:
                f, a, i = f + time[-s[0][1]][2], a if n else max(a, f + time[-s[0][1]][2]), -heapq.heappop(s)[1]
                if n:
                    heapq.heappush(l, (f + time[i][3], i))
            else:
                f, n = f + time[-m[0][1]][0], n - 1
                heapq.heappush(r, (f + time[-m[0][1]][1], -heapq.heappop(m)[1]))
        return a

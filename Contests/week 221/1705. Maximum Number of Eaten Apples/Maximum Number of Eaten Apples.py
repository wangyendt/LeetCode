#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Number of Eaten Apples
@time: 2020/12/27 12:04
"""

import heapq
from typing import *


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        ret = 0
        pq = []
        for i, (a, d) in enumerate(zip(apples, days)):
            heapq.heappush(pq, [i + d, a])
            #             print(pq)
            while pq:
                h1, h2 = pq[0]
                if h2 > 0:
                    if h1 > i:
                        pq[0][1] -= 1
                        ret += 1
                        break
                    else:
                        heapq.heappop(pq)
                else:
                    heapq.heappop(pq)
        #             print(pq,i,ret)
        cur = n
        while pq:
            h1, h2 = pq[0]
            if h2 > 0:
                if h1 > cur:
                    pq[0][1] -= 1
                    ret += 1
                    cur += 1
                else:
                    heapq.heappop(pq)
            else:
                heapq.heappop(pq)
        return ret

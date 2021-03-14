#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Average Pass Ratio.py 
@time: 2021/03/14
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import heapq
from typing import *


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []
        for c1, c2 in classes:
            heapq.heappush(h, ((c1 - c2) / (c2 * (c2 + 1)), c1, c2))
        # print(h)
        for i in range(extraStudents):
            r, c1, c2 = heapq.heappop(h)
            r_ = (c1 - c2) / ((c2 + 1) * (c2 + 2))
            heapq.heappush(h, (r_, c1 + 1, c2 + 1))
            # print(r, c1, c2, h)
        return sum(k[1] / k[2] for k in h) / len(h)


so = Solution()
print(so.maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2))

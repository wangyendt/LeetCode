#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Remove Stones to Minimize the Total.py 
@time: 2021/08/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import math
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)
        for i in range(k):
            p = -heapq.heappop(piles)
            p -= math.floor(p / 2)
            heapq.heappush(piles, -p)
        return -sum(piles)


so = Solution()
print(so.minStoneSum(piles=[5, 4, 9], k=2))

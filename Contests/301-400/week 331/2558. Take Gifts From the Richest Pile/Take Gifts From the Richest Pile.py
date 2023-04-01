#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Take Gifts From the Richest Pile.py 
@time: 2023/02/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq
import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            cur = heapq.heappop(gifts)
            heapq.heappush(gifts, -int(math.floor(math.sqrt(-cur))))
        return -sum(gifts)

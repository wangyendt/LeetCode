#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximal Score After Applying K Operations.py 
@time: 2023/01/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq
import math


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            heapq.heappush(h, -n)
        ret = 0
        for i in range(k):
            s = -heapq.heappop(h)
            ret += s
            heapq.heappush(h, -int(math.ceil(s / 3)))
        return ret

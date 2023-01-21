#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Subsequence Score.py 
@time: 2023/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        h = []
        cur = 0
        ret = 0
        for n1, n2 in sorted(zip(nums1, nums2), key=lambda x: -x[1]):
            heapq.heappush(h, n1)
            cur += n1
            if len(h) > k:
                cur -= heapq.heappop(h)
            if len(h) == k:
                ret = max(ret, cur * n2)
        return ret

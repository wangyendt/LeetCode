#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Distance Between a Pair of Values.py 
@time: 2021/05/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ret = 0
        n2 = len(nums2)
        nums2_neg = nums2[::-1]
        for i, n1 in enumerate(nums1):
            idx = bisect.bisect_left(nums2_neg, n1, hi=n2 - 1 - i)
            ret = max(ret, n2 - 1 - idx - i)
        return ret

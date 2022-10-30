#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Pairs Satisfying Inequality.py 
@time: 2022/10/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import bisect
from sortedcontainers import SortedList


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        diff_arr = [n1 - n2 for n1, n2 in zip(nums1, nums2)]
        l = SortedList()
        ret = 0
        for i, d in enumerate(diff_arr):
            ret += l.bisect_right(d + diff)
            l.add(d)
        return ret


so = Solution()
print(so.numberOfPairs(nums1=[3, 2, 5], nums2=[2, 2, 1], diff=1))
print(so.numberOfPairs(nums1=[3, -1], nums2=[-2, 2], diff=-1))

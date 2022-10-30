#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Good Triplets in an Array.py 
@time: 2022/02/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *

import sys

sys.path.append('..')
from Tools.FenwickTree import *


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        d = {x: i for i, x in enumerate(nums1)}
        arr = [d[nums2[i]] for i in range(n)]
        BIT1, BIT2, ret = FenwickTree(n), FenwickTree(n), 0
        for a in arr:
            ret += BIT2.query(a)
            BIT1.update(a + 1, 1)
            less = BIT1.query(a)
            BIT2.update(a + 1, less)
        return ret


so = Solution()
print(so.goodTriplets(nums1=[2, 0, 1, 3], nums2=[0, 1, 2, 3]))
print(so.goodTriplets(nums1=[4, 0, 1, 3, 2], nums2=[4, 1, 0, 2, 3]))

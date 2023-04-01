#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Operations to Make Array Equal II.py 
@time: 2023/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if sum(nums1) != sum(nums2):
            return -1
        if k == 0:
            if all(n1 == n2 for n1, n2 in zip(nums1, nums2)):
                return 0
            return -1
        cur = 0
        for n1, n2 in zip(nums1, nums2):
            if abs(n1 - n2) % k != 0:
                return -1
            cur += abs(n1 - n2)
        if cur % k != 0: return -1
        return cur // k // 2


so = Solution()
print(so.minOperations(nums1=[10, 5, 15, 20], nums2=[20, 10, 15, 5], k=0))

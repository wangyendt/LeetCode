#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Bitwise XOR of All Pairings.py 
@time: 2022/10/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ret = 0
        if len(nums1) & 1:
            for n in nums2:
                ret ^= n
        if len(nums2) & 1:
            for n in nums1:
                ret ^= n
        return ret


so = Solution()
print(so.xorAllNums(nums1=[2, 1, 3], nums2=[10, 2, 5, 0]))

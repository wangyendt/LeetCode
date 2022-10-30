#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Two Out of Three.py
@time: 2021/10/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
        res = collections.Counter()
        for n1 in nums1:
            res[n1] += 1
        for n2 in nums2:
            res[n2] += 1
        for n3 in nums3:
            res[n3] += 1
        ret = []
        for k, v in res.items():
            if v >= 2:
                ret.append(k)
        return ret

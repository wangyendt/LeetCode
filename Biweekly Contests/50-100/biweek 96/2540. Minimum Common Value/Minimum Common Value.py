#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Common Value.py 
@time: 2023/01/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""



from typing import *
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        A = set(nums1)
        B = set(nums2)
        C = A & B
        if C:
            return sorted(C)[0]
        return -1

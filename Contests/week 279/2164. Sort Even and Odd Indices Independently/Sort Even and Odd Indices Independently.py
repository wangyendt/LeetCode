#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sort Even and Odd Indices Independently.py 
@time: 2022/02/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a1 = [n for i, n in enumerate(nums) if i & 1]
        a2 = [n for i, n in enumerate(nums) if not (i & 1)]
        a1.sort(reverse=True)
        a2.sort()
        ret = []
        for aa1, aa2 in zip(a1, a2):
            ret.append(aa2)
            ret.append(aa1)
        if len(a2) > len(a1):
            ret.append(a2[-1])
        return ret

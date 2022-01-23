#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Rearrange Array Elements by Sign.py 
@time: 2022/01/23
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        r1, r2 = [], []
        for n in nums:
            if n > 0:
                r1.append(n)
            else:
                r2.append(n)
        ret = []
        for s1, s2 in zip(r1, r2):
            ret.append(s1)
            ret.append(s2)
        return ret

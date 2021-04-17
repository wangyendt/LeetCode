#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum XOR for Each Query.py 
@time: 2021/04/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ret = []
        res = 0
        t = (1 << maximumBit) - 1
        # print(t)
        for n in nums:
            res ^= n
            ret.append(res ^ t)
        return ret[::-1]


so = Solution()
print(so.getMaximumXor(nums=[0, 1, 1, 3], maximumBit=2))

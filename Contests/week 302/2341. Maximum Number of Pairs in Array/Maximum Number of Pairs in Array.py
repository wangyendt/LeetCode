#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Number of Pairs in Array.py 
@time: 2022/07/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ret = [0, 0]
        for k, v in collections.Counter(nums).items():
            if v >= 2:
                m, r = divmod(v, 2)
                ret[0] += m
                ret[1] += r
            else:
                ret[1] += v
        return ret


so = Solution()
print(so.numberOfPairs([1, 3, 2, 1, 3, 2, 2]))

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Excellent Pairs.py 
@time: 2022/07/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        c = collections.defaultdict(int)
        for i, num in enumerate(nums):
            m, n = 0, num
            while n:
                m += 1
                n = n & (n - 1)
            c[m] += 1
        # print(c)
        return sum(c[k1] * c[k2] for k1 in c for k2 in c if k1 + k2 >= k)


so = Solution()
print(so.countExcellentPairs(nums=[1, 2, 3, 1], k=3), 5)
# print(so.countExcellentPairs([1, 2, 3, 1, 536870911], 3), 12)

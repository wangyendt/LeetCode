#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Replace Non-Coprime Numbers in Array.py 
@time: 2022/03/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import math
import functools


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        @functools.lru_cache(None)
        def gcd(a1, b1):
            return math.gcd(a1, b1)

        for n in nums:
            cur = n
            while stack:
                prev = stack[-1]
                if gcd(prev, cur) > 1:
                    cur = prev * cur // gcd(prev, cur)
                    stack.pop()
                else:
                    break
            stack.append(cur)
        return stack


so = Solution()
print(so.replaceNonCoprimes(nums=[6, 4, 3, 2, 7, 6, 2]))

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Good Meals.py 
@time: 2021/01/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections
import math


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        def next_pow(a):
            if a == 0:
                return 0
            return (a - 1).bit_length()

        def nchoose2(n):
            return n * (n - 1) // 2

        A = deliciousness
        A.sort()
        cnter = collections.Counter(A)
        ret = 0
        for k, v in cnter.items():
            for i in range(next_pow(2 * k), 22):
                target = 2 ** i - k
                if target in cnter:
                    if k == target:
                        ret += nchoose2(cnter[k])
                    else:
                        if target > A[-1]:
                            break
                        ret += cnter[k] * cnter[target]
        return ret % (10 ** 9 + 7)


so = Solution()
# print(so.countPairs([1, 1, 1, 3, 3, 3, 7]))
print(so.countPairs([149, 107, 1, 63, 0, 1, 6867, 1325, 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]))

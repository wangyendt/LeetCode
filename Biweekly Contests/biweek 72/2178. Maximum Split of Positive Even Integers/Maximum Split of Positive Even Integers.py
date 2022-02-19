#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Split of Positive Even Integers.py 
@time: 2022/02/19
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import math


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        if finalSum == 2: return [2]
        if finalSum == 4: return [4]
        if finalSum == 6: return [2, 4]
        if finalSum == 8: return [2, 6]
        if finalSum == 10: return [2, 8]
        t = finalSum // 2
        l, r = 1, finalSum
        res = 0
        while l < r:
            m = (l + r) // 2
            s1 = m * (m + 1) // 2
            s2 = (m + 1) * (m + 2) // 2
            rest = t - s1
            # print(l, r, m, s1, rest)
            if rest > m and t - s2 <= m + 1:
                res = m
                break
            if rest == 0:
                res = m
                break
            if rest <= m:
                r = m
            elif rest > m:
                l = m + 1
            res = m
        # print(l, m, r, res)
        ret = [2 * (i + 1) for i in range(res)]
        diff = finalSum - sum(ret)
        if diff > 0:
            ret.append(finalSum - sum(ret))
        return ret


so = Solution()
print(so.maximumEvenSplit(12))
print(so.maximumEvenSplit(28))
print(so.maximumEvenSplit(30))
print(so.maximumEvenSplit(32))
print(so.maximumEvenSplit(34))
print(so.maximumEvenSplit(36))
print(so.maximumEvenSplit(38))
print(so.maximumEvenSplit(40))
print(so.maximumEvenSplit(42))
print(so.maximumEvenSplit(44))
print(so.maximumEvenSplit(46))
print(so.maximumEvenSplit(48))
# print(so.maximumEvenSplit(4888888888))

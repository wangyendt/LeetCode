#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count the Number of Ideal Arrays.py 
@time: 2022/07/10
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from math import comb


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10 ** 9 + 7
        ans = maxValue
        freq = {x: 1 for x in range(1, maxValue + 1)}
        for k in range(1, n):
            temp = collections.Counter()
            for x in freq:
                for m in range(2, maxValue // x + 1):
                    ans += comb(n - 1, k) * freq[x]
                    temp[m * x] += freq[x]
            freq = temp
            ans %= 1_000_000_007
        return ans


so = Solution()
print(so.idealArrays(n=2, maxValue=5))
print(so.idealArrays(n=5, maxValue=3))
print(so.idealArrays(n=2, maxValue=15))
print(so.idealArrays(5878, 2900))
print(so.idealArrays(10000, 10000))

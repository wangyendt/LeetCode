#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Ways to Reach a Position After Exactly k Steps.py 
@time: 2022/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from math import comb
from math import perm


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if startPos > endPos:
            startPos, endPos = endPos, startPos
        if k < endPos - startPos:
            return 0
        if k == endPos - startPos:
            return 1
        if (k - (endPos - startPos)) % 2 == 1: return 0
        diff = endPos - startPos
        n_right = diff + (k - diff) // 2
        n_left = (k - diff) // 2
        if n_left == 1:
            return n_right + 1
        return comb(n_right + n_left, n_left) % (10 ** 9 + 7)


so = Solution()
print(so.numberOfWays(startPos=1, endPos=2, k=3))
print(so.numberOfWays(272, 270, 6))

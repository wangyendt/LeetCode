#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Number of Swaps to Make the String Balanced.py 
@time: 2021/08/08
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import math


class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        res = [[0, 0], [0, 0]]
        for i, t in enumerate(s):
            if t == '[':
                res[0][0] += 1
            else:
                if res[0][0] == 0:
                    res[0][1] += 1
                else:
                    res[0][0] -= 1
        return math.ceil(res[0][1] / 2)


so = Solution()
print(so.minSwaps('[]]][['))
import random

s = [t for t in '[' * 20 + ']' * 20]
random.shuffle(s)
print(so.minSwaps(''.join(s)))

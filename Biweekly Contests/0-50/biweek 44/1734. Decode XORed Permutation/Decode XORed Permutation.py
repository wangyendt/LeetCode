#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Decode XORed Permutation.py 
@time: 2021/01/23
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        res = 0
        for i in range(1, len(encoded) + 2):
            res ^= i
        last = 0
        for enc in encoded[::2]:
            last ^= enc
        ret = [last ^ res]
        for enc in encoded[::-1]:
            ret.append(ret[-1] ^ enc)
        return ret[::-1]


so = Solution()
print(so.decode(encoded=[6, 5, 4, 6]))

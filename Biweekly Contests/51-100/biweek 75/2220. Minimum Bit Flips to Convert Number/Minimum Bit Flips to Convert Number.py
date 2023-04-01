#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Bit Flips to Convert Number.py 
@time: 2022/04/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        sb, gb = bin(start)[2:], bin(goal)[2:]
        l = max(len(sb), len(gb))
        sb = '0' * (l - len(sb)) + sb
        gb = '0' * (l - len(gb)) + gb
        # print(sb, gb)
        return sum(1 for s, g in zip(sb, gb) if s != g)


so = Solution()
print(so.minBitFlips(start=10, goal=7))

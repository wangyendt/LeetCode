#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: The Number of Weak Characters in the Game.py 
@time: 2021/09/05
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        n = len(properties)
        mx = collections.defaultdict(int)
        for p1, p2, in properties:
            mx[p1] = max(mx[p1], p2)
        s = sorted(set([p[0] for p in properties]), reverse=True)
        MX = 0
        last = 0
        q = 0
        ret = 0
        for p1, p2 in sorted(properties, reverse=True):
            if MX == 0:
                MX = mx[last]
            if p1 != s[q]:
                q += 1
                MX = max(MX, mx[s[q - 1]])
            # print(p1, p2, s[max(0, q - 1)], MX, last)
            if p1 < s[max(0, q - 1)]:
                if p2 < MX:
                    # print(p1, p2, MX)
                    ret += 1
                last = p1
        return ret


so = Solution()
# print(so.numberOfWeakCharacters(properties=[[5, 5], [6, 3], [3, 6]]))
# print(so.numberOfWeakCharacters([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(so.numberOfWeakCharacters([[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]]))

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Check Distances Between Same Letters.py 
@time: 2022/09/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        res = collections.defaultdict(list)
        for i, t in enumerate(s):
            res[(ord(t) - ord('a'))].append(i)
        ret = True
        for k, vl in res.items():
            if abs(vl[1] - vl[0] - 1) != distance[k]:
                ret = False
                break
        return ret


so = Solution()
print(so.checkDistances(s="abaccb", distance=[1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

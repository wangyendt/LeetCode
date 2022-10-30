#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Players With Zero or One Losses.py 
@time: 2022/04/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        r1, r2 = collections.defaultdict(int), collections.defaultdict(int)
        for mw, ml in matches:
            r1[mw] += 1
            r2[ml] += 1
        ret = [set(), set()]
        for rr1 in r1:
            if r2[rr1] == 0:
                ret[0].add(rr1)
            if r2[rr1] == 1:
                ret[1].add(rr1)
        for rr2 in r2:
            if r2[rr2] == 1:
                ret[1].add(rr2)
        ret[0] = list(sorted(ret[0]))
        ret[1] = list(sorted(ret[1]))
        return ret

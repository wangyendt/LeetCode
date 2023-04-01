#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Node With Highest Edge Score.py 
@time: 2022/10/07
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        res = collections.defaultdict(int)
        for i, e in enumerate(edges):
            res[e] += i
        # print(res)
        return sorted(res.items(), key=lambda x: (-x[1], x[0]))[0][0]


so = Solution()
print(so.edgeScore(edges=[1, 0, 0, 0, 0, 7, 7, 5]))

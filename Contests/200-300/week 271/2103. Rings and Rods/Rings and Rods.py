#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Rings and Rods.py 
@time: 2021/12/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def countPoints(self, rings: str) -> int:
        res = collections.defaultdict(set)
        n = len(rings)
        for i in range(0, n, 2):
            # print(i, n)
            res[rings[i + 1]].add(rings[i])
        ret = 0
        # print(res)
        for i in range(10):
            if len(res[str(i)]) == 3:
                ret += 1
        return ret


so = Solution()
print(so.countPoints(rings="B0B6G0R6R0R6G9"))

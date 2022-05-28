#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Total Importance of Roads.py 
@time: 2022/05/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections
from typing import *


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        res = collections.defaultdict(int)
        for l, r in roads:
            res[l] += 1
            res[r] += 1
        res2 = [r[1] for r in sorted(res.items(), key=lambda x: x[1], reverse=True)]
        # print(res2)
        ret = 0
        p = n
        for i in range(len(res2)):
            ret += p * res2[i]
            p -= 1
        return ret


so = Solution()
print(so.maximumImportance(n=5, roads=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
print(so.maximumImportance(5, [[0, 1]]))

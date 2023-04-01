#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Rows Covered by Columns.py 
@time: 2022/09/03
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import itertools
import collections


class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        ret = 0
        for item in itertools.combinations(range(n), cols):
            res = 0
            for j in range(m):
                if all(mat[j][t] == 0 for t in set(range(n)) - set(item)):
                    res += 1
            ret = max(res, ret)
        return ret


so = Solution()
print(so.maximumRows(mat=[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], cols=2))

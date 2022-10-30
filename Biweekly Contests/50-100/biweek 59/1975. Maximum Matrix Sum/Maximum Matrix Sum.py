#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Matrix Sum.py 
@time: 2021/08/21
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = []
        for i in range(n):
            for j in range(n):
                res.append(matrix[i][j])
        cnt = 0
        for r in res:
            if r == 0:
                return sum([abs(r) for r in res])
            if r < 0:
                cnt = 1 - cnt

        if cnt == 0:
            return sum([abs(r) for r in res])
        return sum([abs(r) for r in res]) - 2 * min([abs(r) for r in res])


so = Solution()
print(so.maxMatrixSum([[10000, 10000, 10000], [10000, 10000, 10000], [10000, 10000, 10000]]))

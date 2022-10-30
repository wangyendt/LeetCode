#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Largest Submatrix With Rearrangements.py 
@time: 2021/01/17
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""
from typing import *
import collections


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if i == 0:
                    res[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 0:
                        res[i][j] = 0
                    else:
                        res[i][j] = res[i - 1][j] + 1
        [print(r) for r in res]
        ret = 0
        for i in range(m):
            cnt = list(sorted(collections.Counter(res[i]).items(), key=lambda x: x[0], reverse=True))
            print(cnt)
            mx = 0
            s = 0
            for k, v in cnt:
                s += v
                if k * s > mx:
                    mx = k * s
            ret = max(ret, mx)
        return ret


so = Solution()
print(so.largestSubmatrix(matrix=[[0, 0, 1], [1, 1, 1], [1, 0, 1]]))

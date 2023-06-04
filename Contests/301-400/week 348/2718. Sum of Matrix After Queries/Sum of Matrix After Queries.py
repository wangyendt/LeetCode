#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Sum of Matrix After Queries.py 
@time: 2023/06/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_cnt, col_cnt = 0, 0
        ret = 0
        row_seen, col_seen = set(), set()
        for i, (t, idx, val) in enumerate(queries[::-1]):
            if t == 0:
                if idx in row_seen:
                    continue
                row_seen.add(idx)
                ret += (n - col_cnt) * val
                row_cnt += 1
            else:
                if idx in col_seen:
                    continue
                col_seen.add(idx)
                ret += (n - row_cnt) * val
                col_cnt += 1
        return ret


so = Solution()
print(so.matrixSumQueries(n=3, queries=[[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]))

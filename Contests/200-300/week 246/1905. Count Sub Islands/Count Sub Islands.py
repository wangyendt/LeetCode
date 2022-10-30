#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Sub Islands.py 
@time: 2021/06/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import collections


class Solution:
    def countSubIslands(self, A1: List[List[int]], A2: List[List[int]]) -> int:
        m, n = len(A1), len(A1[0])
        isl_id = collections.defaultdict(list)
        cnt = 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if A2[i][j] == 0:
                    continue
                if (i, j) in seen:
                    continue
                cnt += 1
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    seen.add((r, c))
                    isl_id[cnt].append((r, c))
                    for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= rr < m and 0 <= cc < n:
                            if A2[rr][cc] == 0:
                                continue
                            else:
                                if (rr, cc) not in seen:
                                    stack.append((rr, cc))
        # print(cnt)
        ret = 0
        for k, v in isl_id.items():
            if all(A1[v1][v2] == 1 for v1, v2 in v):
                ret += 1
        return ret


so = Solution()
print(so.countSubIslands(
    [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
    [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
))

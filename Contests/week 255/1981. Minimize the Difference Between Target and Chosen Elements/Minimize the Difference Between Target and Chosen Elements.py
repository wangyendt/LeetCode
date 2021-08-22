#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimize the Difference Between Target and Chosen Elements.py 
@time: 2021/08/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import functools
import bisect


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        inf = float('inf')

        mn, mx = [], []
        for i, mt in enumerate(mat):
            if i == 0:
                mn.append(min(mt))
                mx.append(max(mt))
            else:
                mn.append(mn[-1] + min(mt))
                mx.append(mx[-1] + max(mt))

        # print(mx)
        A0 = mat[0]
        A0.sort()

        @functools.lru_cache(None)
        def dp(i, k):
            if k >= mx[i]: return abs(mx[i] - k), mx[i]
            if k <= mn[i]: return abs(mn[i] - k), mn[i]
            if i == 0:
                ret1, ret2 = inf, -inf
                idx = bisect.bisect_left(A0, k)
                for jdx in (idx, idx - 1):
                    res = abs(mat[i][jdx] - k)
                    if ret1 > res:
                        ret1 = res
                        ret2 = mat[i][jdx]
                return ret1, ret2
            else:
                ret1, ret2 = inf, -inf
                for mj in set(mat[i]):
                    m1 = -mj + k
                    res1, res2 = dp(i - 1, m1)
                    if res1 == 0: return 0, 0
                    n1 = abs(res2 + mj - k)
                    if ret1 > n1:
                        ret1 = n1
                        ret2 = res2 + mj
                    m2 = -mj - k
                    res1, res2 = dp(i - 1, m2)
                    if res1 == 0: return 0, 0
                    n2 = abs(res2 + mj - k)
                    if ret1 > n2:
                        ret1 = n2
                        ret2 = res2 + mj
                return ret1, ret2

        return dp(m - 1, target)[0]


so = Solution()
print(so.minimizeTheDifference(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], target=13))
print(so.minimizeTheDifference(mat=[[1], [2], [3]], target=100))
print(so.minimizeTheDifference(mat=[[1, 2, 3]], target=100))
print(so.minimizeTheDifference(mat=[[i + j for j in range(70)] for i in range(70)], target=100000))
# def dp(i,j,k):
#     if i==0:
#         res = 1000
#         for t in range(j+1):
#             res = min(res,abs(k-mat[i][j]))
#         return res
#     if j == 0:
#         res = 1000
#         for t in range(i+1):
#             res = min(res,abs(k-mat[i][j]))
#         return  res
#     return min(
#         dp(i-1,j-1)
#     )
#
# return dp(m-1,n-1,target)

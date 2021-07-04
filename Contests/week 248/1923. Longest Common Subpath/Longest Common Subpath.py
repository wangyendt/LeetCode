#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Longest Common Subpath.py 
@time: 2021/07/04
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def RabinKarp(arr, M, q):
            h, t, d = (1 << (17 * M - 17)) % q, 0, 1 << 17
            all_hashes = set()

            for i in range(M):
                t = (d * t + arr[i]) % q

            all_hashes.add(t)

            for i in range(len(arr) - M):
                t = (d * (t - arr[i] * h) + arr[i + M]) % q
                all_hashes.add(t)

            return all_hashes

        m, mod = len(paths), (1 << 128) - 159
        beg, end = 0, min(len(p) for p in paths) + 1

        while beg + 1 < end:
            mid = (beg + end) // 2
            tt = set.intersection(*[RabinKarp(p, mid, mod) for p in paths])

            if len(tt) != 0:
                beg = mid
            else:
                end = mid

        return beg

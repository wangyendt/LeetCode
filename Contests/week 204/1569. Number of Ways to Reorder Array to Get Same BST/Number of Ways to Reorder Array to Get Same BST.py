#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Number of Ways to Reorder Array to Get Same BST.py 
@time: 2020/08/31
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

from scipy.special import comb


class Solution:
    def numOfWays(self, A: list) -> int:
        mod = 10 ** 9 + 7

        def split(left, right):
            lnum, rnum = 1, 1
            if left:
                lroot = left[0]
                lnum = split([l for l in left if l < lroot], [r for r in left if r > lroot])
            if right:
                rroot = right[0]
                rnum = split([l for l in right if l < rroot], [r for r in right if r > rroot])
            return lnum * rnum * comb(len(left) + len(right), len(left))

        root = A[0]
        return split([l for l in A if l < root], [r for r in A if r > root]) % mod - 1

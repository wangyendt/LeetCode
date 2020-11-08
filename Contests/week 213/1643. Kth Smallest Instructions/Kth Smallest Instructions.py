#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Kth Smallest Instructions.py 
@time: 2020/11/01
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *
import math
import functools


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        row, col = destination

        @functools.lru_cache(None)
        def variants(r, c):  # number of different paths from point (r,c) to the destination
            if r == row or c == col:  # if already last row or column - only one choise left
                return 1
            if r > row or c > col:
                return 0
            return variants(r + 1, c) + variants(r, c + 1)  # sum of paths if we go right and paths if we go down

        res = ''
        i = 0  # start row
        j = 0  # start col
        while len(res) < row + col:  # the final path length is (row + col + 1)
            if j == col:  # nowhere else to go - only down
                res += 'V'
            elif i == row:  # already last row, go right
                res += 'H'
            else:
                if variants(i, j + 1) >= k:
                    res += 'H'
                    j += 1
                else:
                    k -= variants(i, j + 1)  # we didn't go right so we lost all possibilities there
                    res += 'V'
                    i += 1

        return res


so = Solution()
# print(so.kthSmallestPath(destination=[2, 3], k=1))
# print(so.kthSmallestPath(destination=[15, 15], k=10000))
print(so.kthSmallestPath(destination=[1, 1], k=2))
print(so.kthSmallestPath([15, 15], 155117520))

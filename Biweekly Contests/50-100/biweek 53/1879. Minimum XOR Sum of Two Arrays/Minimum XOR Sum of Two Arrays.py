#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum XOR Sum of Two Arrays.py 
@time: 2021/05/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        from scipy.optimize import linear_sum_assignment
        n = len(nums1)
        cost = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                cost[i][j] = nums1[i] ^ nums2[j]

        row_ind, col_ind = linear_sum_assignment(cost)
        res = 0
        for i, j in zip(row_ind, col_ind):
            res += cost[i][j]
        return res


so = Solution()
print(so.minimumXORSum(nums1=[1, 2], nums2=[2, 3]))
print(so.minimumXORSum([5988718, 8234413, 7045869, 2043465, 3505519, 9572150, 6429975, 3436338, 4765525, 1814274],
                       [405180, 1980911, 9551412, 221727, 9148399, 4972978, 2291667, 1261371, 8394840, 6270103]))
print(so.minimumXORSum(
    [9606269, 5221932, 7334481, 8439484, 5986425, 8864979, 5430580, 14172, 2078710, 7420803, 7542233],
    [5875595, 5113681, 9047874, 6700866, 5693602, 9586753, 8259408, 1897425, 6334375, 6415366, 3421110]
))

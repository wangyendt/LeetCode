#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Matrix Diagonal Sum.py 
@time: 2020/09/05
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def diagonalSum(self, mat: list(list())) -> int:
        m = len(mat)
        ret = 0
        for i in range(m):
            ret += mat[i][i] + mat[i][~i]
        if m % 2 == 1:
            ret -= mat[m // 2][m // 2]
        return ret

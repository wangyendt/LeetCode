#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Determine Whether Matrix Can Be Obtained By Rotation.py 
@time: 2021/06/06
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(matrix):
            matrix = matrix[::-1]  # 先反转
            rows, cols = len(matrix), len(matrix[0])
            for i in range(rows):  # 做转置，对角线不交换，把右上三角换到左下三角
                for j in range(i, cols):  # 注意从i开始，不要换了又把左下三角换回去了
                    if i == j:
                        continue
                    else:
                        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix

        for i in range(4):
            mat = rotate(mat)
            #             [print(m) for m in mat]
            b = True
            for ii in range(n):
                for jj in range(n):
                    if mat[ii][jj] != target[ii][jj]:
                        b = False
                        break
                else:
                    continue
                break
            if b: return True
        return False

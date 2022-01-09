#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: 2133. Check if Every Row and Column Contains All Numbers.py 
@time: 2022/01/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            res = set()
            for j in range(n):
                res.add(matrix[i][j])
                if len(res) != j + 1:
                    return False
        for j in range(n):
            res = set()
            for i in range(m):
                res.add(matrix[i][j])
                if len(res) != i + 1:
                    return False
        return True


so = Solution()
print(so.checkValid(matrix=[[1, 1, 1], [1, 2, 3], [1, 2, 3]]))

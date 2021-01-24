#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Find Kth Largest XOR Coordinate Value.py 
@time: 2021/01/24
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        rows = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    rows[i][j] = matrix[i][j]
                else:
                    rows[i][j] = rows[i][j - 1] ^ matrix[i][j]
        cols = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    cols[i][j] = rows[i][j]
                else:
                    cols[i][j] = cols[i - 1][j] ^ rows[i][j]
        # print(cols)
        stack = []
        # [print(r) for r in cols]
        for i in range(m):
            for j in range(n):
                stack.append(cols[i][j])
        stack.sort(reverse=True)
        return stack[k - 1]


print(5 ^ 2 ^ 1 ^ 6)
so = Solution()
print(so.kthLargestValue(matrix=[[5, 2], [1, 6]], k=3))

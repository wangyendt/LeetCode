#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Height by Stacking Cuboids
@time: 2020/12/13 11:26
"""

from typing import *


class Solution:
    def maxHeight(self, arr: List[List[int]]) -> int:
        A = [[0, 0, 0]] + sorted(map(sorted, arr))
        dp = [0] * len(A)
        for j in range(1, len(A)):
            for i in range(j):
                if all(A[i][k] <= A[j][k] for k in range(3)):
                    dp[j] = max(dp[j], dp[i] + A[j][2])
        return max(dp)


so = Solution()
print(so.maxHeight([[50, 45, 20], [95, 37, 53], [45, 23, 12]]))
print(so.maxHeight([[38, 25, 45], [76, 35, 3]]))
print(so.maxHeight([[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]))
print(so.maxHeight([[26, 38, 38], [37, 93, 79]]))

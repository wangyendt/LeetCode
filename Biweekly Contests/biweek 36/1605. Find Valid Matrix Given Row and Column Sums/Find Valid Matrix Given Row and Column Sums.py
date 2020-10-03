#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Valid Matrix Given Row and Column Sums
@time: 2020/10/03 22:53
"""

from typing import *
import sys


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        ret = [[-1 for _ in range(n)] for _ in range(m)]
        inf = sys.maxsize
        cnt = m * n
        while cnt > 0:
            mr, mc = min(rowSum), min(colSum)
            # print(rowSum, colSum, mr, mc)
            mri, mci = rowSum.index(mr), colSum.index(mc)
            if mr > mc:
                for j in range(m):
                    if ret[j][mci] == -1:
                        ret[j][mci] = 0
                        cnt -= 1
                ret[mri][mci] = mc
                mr -= mc
                colSum[mci] = inf
                rowSum[mri] -= mc
            else:
                for j in range(n):
                    if ret[mri][j] == -1:
                        ret[mri][j] = 0
                        cnt -= 1
                ret[mri][mci] = mr
                mc -= mr
                rowSum[mri] = inf
                colSum[mci] -= mr
            # print(ret)
        return ret


so = Solution()
# print(so.restoreMatrix(rowSum=[3, 8], colSum=[4, 7]))
print(so.restoreMatrix(rowSum=[1, 0], colSum=[1]))

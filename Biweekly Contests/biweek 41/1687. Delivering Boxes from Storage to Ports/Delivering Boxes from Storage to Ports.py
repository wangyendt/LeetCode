#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Delivering Boxes from Storage to Ports
@time: 2020/12/12 22:51
"""

from typing import *


class Solution:
    def boxDelivering(self, A: List[List[int]], portsCount: int, maxB: int, maxW: int) -> int:
        n = len(A)
        curP = curB = curW = j = 0
        j = lastj = -1
        res = [0] + [float('inf')] * n
        for i in range(n):
            while j + 1 < n and curB + 1 <= maxB and curW + A[j + 1][1] <= maxW:
                j += 1
                curB += 1
                curW += A[j][1]
                if j == 0 or A[j][0] != A[j - 1][0]:
                    lastj = j
                    curP += 1
                res[j + 1] = min(res[j + 1], res[i] + curP + 1)

            res[j + 1] = min(res[j + 1], res[i] + curP + 1)
            res[lastj] = min(res[lastj], res[i] + curP)

            curB -= 1
            curW -= A[i][1]
            if i == n - 1 or A[i][0] != A[i + 1][0]:
                curP -= 1
            i += 1
        return res[-1]

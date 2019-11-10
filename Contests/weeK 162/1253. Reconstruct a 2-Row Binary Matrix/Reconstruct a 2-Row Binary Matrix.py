#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Reconstruct a 2-Row Binary Matrix
@time: 2019/11/10 21:29
"""


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: list) -> list(list()):
        n = len(colsum)
        ret = [[0 for _ in range(n)] for _ in range(2)]
        for i in range(n):
            if colsum[i] == 0:
                continue
            elif colsum[i] == 1:
                if upper > lower:
                    ret[0][i] = 1
                    upper -= 1
                else:
                    ret[1][i] = 1
                    lower -= 1
            elif colsum[i] == 2:
                ret[0][i] = 1
                ret[1][i] = 1
                upper -= 1
                lower -= 1
            else:
                return []
        if upper == lower == 0:
            return ret
        else:
            return []


so = Solution()
print(so.reconstructMatrix(upper=2, lower=1, colsum=[1, 1, 1]))
print(so.reconstructMatrix(upper=2, lower=3, colsum=[2, 2, 1, 1]))
print(so.reconstructMatrix(upper=5, lower=5, colsum=[2, 1, 2, 0, 1, 0, 1, 2, 0, 1]))

#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/17 17:07
@Author:  wang121ye
@File: Simplified Fractions.py
@Software: PyCharm
"""


class Solution:
    def simplifiedFractions(self, n: int) -> list:
        def gca(a, b):
            if a < b: a, b = b, a
            if b == 0: return a
            m, r = divmod(a, b)
            return gca(r, b)

        ret = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if gca(i, j) == 1:
                    ret.append(f'{j}/{i}')
        return ret


so = Solution()
print(so.simplifiedFractions(2))
print(so.simplifiedFractions(3))
print(so.simplifiedFractions(4))
print(so.simplifiedFractions(1))

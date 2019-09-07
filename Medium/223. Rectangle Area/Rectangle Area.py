# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/7 17:05
# software: PyCharm


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        S = (C - A) * (D - B) + (G - E) * (H - F)
        if C <= E or G <= A or D <= F or H <= B:
            return S
        else:
            X = sorted((A, C, E, G))
            Y = sorted((B, D, F, H))
            x1, x2 = X[1], X[2]
            y1, y2 = Y[1], Y[2]
            return S - (x2 - x1) * (y2 - y1)


so = Solution()
print(so.computeArea(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2))

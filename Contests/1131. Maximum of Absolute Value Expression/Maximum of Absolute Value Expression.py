#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Maximum of Absolute Value Expression.py 
@time: 2019/07/22
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def maxAbsValExpr(self, x, y):
        ret, n = 0, len(x)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            closest = p * x[0] + q * y[0] + 0
            for i in range(n):
                cur = p * x[i] + q * y[i] + i
                ret = max(ret, cur - closest)
                closest = min(closest, cur)
        return ret


so = Solution()
print(so.maxAbsValExpr(x=[1, -2, -5, 0, 10], y=[0, -2, -1, -7, -4]))

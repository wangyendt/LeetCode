#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Number of Equivalent Domino Pairs.py 
@time: 2019/07/21
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import collections


class Solution:
    def numEquivDominoPairs(self, dominoes: list(list())) -> int:
        for di in range(len(dominoes)):
            p, q = dominoes[di]
            dominoes[di] = (q, p) if p > q else (p, q)
        cnt = [c for c in collections.Counter(dominoes).items() if c[1] > 1]
        if not cnt:
            return 0
        else:
            return sum(l[1] * (l[1] - 1) // 2 for l in cnt)


so = Solution()
print(so.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))

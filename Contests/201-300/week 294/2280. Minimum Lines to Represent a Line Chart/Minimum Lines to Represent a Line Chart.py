#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Lines to Represent a Line Chart.py 
@time: 2022/05/22
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        ret = 0
        last = (-325422, 6236277)
        stockPrices.sort(key=lambda x: x[0])
        if len(stockPrices) == 2: return 1
        for i, (d, p) in enumerate(stockPrices):
            if i == 0: continue
            cur = (p - stockPrices[i - 1][1], d - stockPrices[i - 1][0])
            if cur[1] * last[0] != cur[0] * last[1]:
                ret += 1
            last = cur
        return ret

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Closest Dessert Cost.py 
@time: 2021/02/28
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *

import itertools


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = set()
        for items in itertools.product(range(3), repeat=len(toppingCosts)):
            s = 0
            for item, tc in zip(items, toppingCosts):
                s += item * tc
            res.add(s)
        mems = set()
        # print(res)
        for bc in baseCosts:
            for r in res:
                mems.add(bc + r)
        mems = list(sorted(mems))
        ret = mems[0]
        for m in mems:
            if abs(m - target) < abs(ret - target):
                ret = m
        return ret


so = Solution()
print(so.closestCost(baseCosts=[1, 7], toppingCosts=[3, 4], target=10))
print(so.closestCost(baseCosts=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                     toppingCosts=[3, 2, 3, 4, 5, 6, 7, 8, 9, 10], target=10))
print(so.closestCost(baseCosts=[2, 3], toppingCosts=[4, 5, 100], target=18))

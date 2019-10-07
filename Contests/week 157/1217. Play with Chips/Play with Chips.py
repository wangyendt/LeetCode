#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Play with Chips.py 
@time: 2019/10/07
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def minCostToMoveChips(self, chips: list) -> int:
        cost1 = sum([c for i, c in enumerate(chips) if i % 2 == 0])
        cost2 = sum([c for i, c in enumerate(chips) if i % 2 == 1])
        return min(cost1, cost2)


so = Solution()
print(so.minCostToMoveChips(chips=[1, 2, 3]))
print(so.minCostToMoveChips(chips=[2, 2, 2, 3, 3]))

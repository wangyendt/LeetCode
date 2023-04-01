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
        even_parity = 0
        odd_parity = 0
        for chip in chips:
            if chip % 2 == 0:
                even_parity += 1
            else:
                odd_parity += 1
        return min(even_parity, odd_parity)


so = Solution()
print(so.minCostToMoveChips(chips=[1, 2, 3]))
print(so.minCostToMoveChips(chips=[2, 2, 2, 3, 3]))

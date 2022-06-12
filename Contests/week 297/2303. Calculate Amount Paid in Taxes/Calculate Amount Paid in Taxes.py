#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Calculate Amount Paid in Taxes.py 
@time: 2022/06/12
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ret = 0
        last = 0
        for i, (b_upper, b_tax) in enumerate(brackets):
            ret += min(b_upper - last, income - last) * b_tax / 100
            # print(b_upper, b_tax, ret)
            if income <= b_upper:
                break
            last = b_upper
        return ret


so = Solution()
print(so.calculateTax(brackets=[[3, 50], [7, 10], [12, 25]], income=10))

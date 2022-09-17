#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Minimum Money Required Before Transactions.py 
@time: 2022/09/18
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        res = v = 0
        for i, j in transactions:
            res += max(0, i - j)
            v = max(v, min(i, j))
        return res + v


so = Solution()
print(so.minimumMoney([[7, 2], [0, 10], [5, 0], [4, 1], [5, 8], [5, 9]]))

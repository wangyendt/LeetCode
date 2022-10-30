#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Number of Consecutive Values You Can Make.py 
@time: 2021/03/20
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        next = 0
        for c in coins:
            if c <= next:
                next += c
            else:
                if next == 0:
                    if c == 1:
                        next = 2
                    else:
                        return 1
                else:
                    return next
        return next


so = Solution()
print(so.getMaximumConsecutive(coins=[1, 4, 10, 3, 1]))

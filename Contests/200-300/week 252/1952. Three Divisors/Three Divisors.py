#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Three Divisors.py 
@time: 2021/08/02
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import math


class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1: return False  # edge case

        x = int(math.sqrt(n))
        if x * x != n: return False

        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0: return False
        return True


so = Solution()
print(so.isThree(81))

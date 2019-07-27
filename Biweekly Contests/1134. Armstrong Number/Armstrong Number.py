#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Armstrong Number.py 
@time: 2019/07/27
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def isArmstrong(self, N: int) -> bool:
        m = n = N
        res = 0
        while n:
            res += 1
            n //= 10
        while m and N >= 0:
            N -= (m % 10) ** res
            m //= 10
        return N == 0


so = Solution()
print(so.isArmstrong(153))
print(so.isArmstrong(123))
print(so.isArmstrong(1))
print(so.isArmstrong(2))
print(so.isArmstrong(12))

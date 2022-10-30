#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Calculate Money in Leetcode Bank.py 
@time: 2021/01/09
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        d, r = divmod(n, 7)
        ret = 0
        # print(d, r)
        for i in range(7):
            ret += ((1 + i) + (d + i)) * d // 2
        for j in range(r):
            ret += (d + j + 1)
        return ret


so = Solution()
print(so.totalMoney(4))

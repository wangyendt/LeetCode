#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Count Number of Ways to Place Houses.py 
@time: 2022/06/26
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10 ** 9 + 7

        def dp(i):
            """return 00,10,01,11"""
            if i == 1:
                return 1, 1, 1, 1
            res = dp(i - 1)
            return tuple(map(lambda x: x % mod, (
                res[0] + res[1] + res[2] + res[3],
                res[0] + res[2],
                res[0] + res[1],
                res[0]
            )))

        return sum(dp(n)) % mod

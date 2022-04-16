#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Number of Ways to Buy Pens and Pencils.py 
@time: 2022/04/16
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        n_pens = 0
        ret = 0
        while True:
            rest = total - cost1 * n_pens
            if rest >=0:
                ret += rest // cost2 + 1
            n_pens += 1
            if rest <= 0:
                break
        return ret


so = Solution()
print(so.waysToBuyPensPencils(total=5, cost1=10, cost2=10))
print(so.waysToBuyPensPencils(total=5, cost1=5, cost2=5))
print(so.waysToBuyPensPencils(100, 19, 13))

#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Range Product Queries of Powers.py 
@time: 2022/10/15
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

from typing import *


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        n_bit = bin(n)[2:]
        res = [i for i, n in enumerate(n_bit[::-1]) if n == '1']
        # print(res)
        # print(n_bit)
        presum = [0]
        for r in res:
            presum.append(presum[-1] + r)
        # print(presum)
        ret = []
        mod = 10 ** 9 + 7
        for s, e in queries:
            ret.append(pow(2, presum[e + 1] - presum[s], mod))
        return ret


so = Solution()
print(so.productQueries(n=15, queries=[[0, 1], [2, 2], [0, 3]]))

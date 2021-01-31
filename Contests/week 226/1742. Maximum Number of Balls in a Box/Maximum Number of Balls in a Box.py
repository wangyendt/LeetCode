#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: Maximum Number of Balls in a Box.py 
@time: 2021/01/31
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import collections


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digit_sum(num: int):
            ret = 0
            while num:
                ret += num % 10
                num //= 10
            return ret

        res = collections.defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            res[digit_sum(i)] += 1
        return sorted(res.items(), key=lambda x: x[1])[-1][1]


so = Solution()
print(so.countBalls(1, 10))

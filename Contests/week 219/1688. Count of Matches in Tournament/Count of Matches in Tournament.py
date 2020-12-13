#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Count of Matches in Tournament
@time: 2020/12/13 10:31
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        ret = 0
        while n > 1:
            if n % 2 == 0:
                res = n // 2
                ret += res
                n -= res
            else:
                res = (n - 1) // 2
                ret += res
                n -= res
        return ret

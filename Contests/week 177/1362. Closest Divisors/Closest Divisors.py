#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Closest Divisors
@time: 2020/2/26 17:53
"""

import math


class Solution:
    def closestDivisors(self, num: int) -> list:
        def diff_closest_factors(num: int):
            sqr_n = int(math.sqrt(num))
            if sqr_n ** 2 == num:
                return 0, [sqr_n, sqr_n]
            else:
                n = sqr_n
                while n >= 1:
                    if num % n == 0:
                        return num // n - n, [n, num // n]
                    n -= 1

        res1, ret1 = diff_closest_factors(num + 1)
        res2, ret2 = diff_closest_factors(num + 2)
        return ret1 if res1 < res2 else ret2


so = Solution()
print(so.closestDivisors(8))
print(so.closestDivisors(123))
print(so.closestDivisors(999))
print(so.closestDivisors(99999989))

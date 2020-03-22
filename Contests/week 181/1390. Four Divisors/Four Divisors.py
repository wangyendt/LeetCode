#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/23 1:05
@Author:  wang121ye
@File: Four Divisors.py
@Software: PyCharm
"""

import math


class Solution:
    def sumFourDivisors(self, nums: list) -> int:
        res = 0
        for num in nums:
            divisor = set()
            for i in range(1, math.floor(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisor.add(num // i)
                    divisor.add(i)
                if len(divisor) > 4:
                    break

            if len(divisor) == 4:
                res += sum(divisor)
        return res


so = Solution()
print(so.sumFourDivisors(nums=[21, 4, 7]))
print(so.sumFourDivisors([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

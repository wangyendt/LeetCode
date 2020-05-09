#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/9 16:38
@Author:  wang121ye
@File: Kids With the Greatest Number of Candies.py
@Software: PyCharm
"""


class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        max_candy = max(candies)
        return [c >= max_candy - extraCandies for c in candies]


so = Solution()
print(so.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
print(so.kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
print(so.kidsWithCandies(candies=[12, 1, 12], extraCandies=10))

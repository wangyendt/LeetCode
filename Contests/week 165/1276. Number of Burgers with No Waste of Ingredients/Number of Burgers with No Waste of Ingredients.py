#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Burgers with No Waste of Ingredients
@time: 2019/12/2 17:18
"""


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list:
        # 4x+2y=a
        # x+y=b
        # x=(a-2b)/2
        # y=(4b-a)/2
        a, b = tomatoSlices, cheeseSlices
        if 2 * b <= a <= 4 * b and a % 2 == 0:
            return [(a - 2 * b) // 2, (4 * b - a) // 2]
        return []


so = Solution()
print(so.numOfBurgers(tomatoSlices=16, cheeseSlices=7))
print(so.numOfBurgers(tomatoSlices=17, cheeseSlices=4))
print(so.numOfBurgers(tomatoSlices=4, cheeseSlices=17))
print(so.numOfBurgers(tomatoSlices=0, cheeseSlices=0))
print(so.numOfBurgers(tomatoSlices=2, cheeseSlices=1))

#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Average Salary Excluding the Minimum and Maximum Salary
@time: 2020/06/27 22:30
"""


class Solution:
    def average(self, salary: list) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)


so = Solution()
print(so.average(salary=[4000, 3000, 1000, 2000]))
print(so.average(salary=[1000, 2000, 3000]))
print(so.average(salary=[6000, 5000, 4000, 3000, 2000, 1000]))
print(so.average(salary=[8000, 9000, 2000, 3000, 6000, 1000]))

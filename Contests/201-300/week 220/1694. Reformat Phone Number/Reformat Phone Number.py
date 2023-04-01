#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Reformat Phone Number
@time: 2020/12/20 10:32
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')

        def helper(num: str):
            if len(num) == 2:
                return num
            if len(num) == 3:
                return num
            if len(num) == 4:
                return num[:2] + '-' + num[2:]
            return num[:3] + '-' + helper(num[3:])

        return helper(number)


so = Solution()
print(so.reformatNumber(number="1-23-45 6"))
print(so.reformatNumber(number="123 4-567"))
print(so.reformatNumber(number="123 4-5678"))
# print(so.reformatNumber())

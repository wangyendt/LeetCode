#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/8 20:24
@Author:  wang121ye
@File: Bulb Switcher III.py
@Software: PyCharm
"""


class Solution:
    def numTimesAllBlue(self, light: list) -> int:
        M, ret = 0, 0
        for i, l in enumerate(light):
            M = max(M, l)
            if M == i + 1:
                ret += 1
        return ret


so = Solution()
print(so.numTimesAllBlue([2, 1, 3, 5, 4]))
print(so.numTimesAllBlue([3, 2, 4, 1, 5]))
print(so.numTimesAllBlue([4, 1, 2, 3]))

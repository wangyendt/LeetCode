#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/8 20:17
@Author:  wang121ye
@File: Generate a String With Characters That Have Odd Counts.py
@Software: PyCharm
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'a' * (n - 1) + 'b'
        else:
            return 'a' * n

#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/23 2:16
@Author:  wang121ye
@File: Longest Happy Prefix.py
@Software: PyCharm
"""


class Solution:
    def longestPrefix(self, s: str) -> str:
        res, l, r, mod = 0, 0, 0, 10 ** 9 + 7
        for i in range(len(s) - 1):
            l = (l * 128 + ord(s[i])) % mod
            r = (r + pow(128, i, mod) * ord(s[~i])) % mod
            if l == r: res = i + 1
        return s[:res]

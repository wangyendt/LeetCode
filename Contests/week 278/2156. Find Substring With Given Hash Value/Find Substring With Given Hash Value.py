#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Find Substring With Given Hash Value
@time: 2022/02/01 02:04
"""


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        pp = pow(power, k - 1, modulo)
        hs = ii = 0
        for i, ch in enumerate(reversed(s)):
            if i >= k: hs -= (ord(s[~(i - k)]) - 96) * pp
            hs = (hs * power + (ord(ch) - 96)) % modulo
            if i >= k - 1 and hs == hashValue: ii = i
        return s[~ii:~ii + k or None]

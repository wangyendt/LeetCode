#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Make The String Great
@time: 2020/08/09 18:18
"""


class Solution:
    def makeGood(self, s: str) -> str:
        p = 0
        while p + 1 < len(s):
            a, b = ord(s[p]), ord(s[p + 1])
            if abs(a - b) == 32:
                s = s[:p] + s[p + 2:]
                p = max(0, p - 1)
            else:
                p += 1
        return s


so = Solution()
print(so.makeGood("leEeetcode"))
print(so.makeGood("abBAcC"))
print(so.makeGood("s"))

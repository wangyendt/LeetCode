#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Remove to Make Valid Parentheses
@time: 2019/11/8 15:24
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        q = []
        for i in range(len(s)):
            if s[i] == ")" and len(q) > 0 and q[-1][0] == "(":
                q.pop(-1)
            elif s[i] in ["(", ")"]:
                q.append([s[i], i])

        while len(q) > 0:
            x = q.pop(-1)[1]
            s = s[0:x] + s[x + 1:]

        return s

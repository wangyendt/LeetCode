#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Nesting Depth of the Parentheses
@time: 2020/10/11 12:03
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        ret = 0
        for t in s:
            if t == '(':
                res += 1
                ret = max(ret, res)
            elif t == ')':
                res -= 1
        return ret

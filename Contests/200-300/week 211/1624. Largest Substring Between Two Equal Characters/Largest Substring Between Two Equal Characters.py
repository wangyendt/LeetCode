#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Largest Substring Between Two Equal Characters
@time: 2020/10/18 23:43
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ret = -1
        for i in 'abcdefghijklmnopqrstuvwxyz':
            left = s.find(i)
            right = s.rfind(i)
            if left == right:
                continue
            ret = max(ret, right - left - 1)
        return ret

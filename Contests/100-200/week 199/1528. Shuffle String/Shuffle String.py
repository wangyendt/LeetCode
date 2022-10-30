#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Shuffle String
@time: 2020/07/27 00:55
"""


class Solution:
    def restoreString(self, s: str, indices: list) -> str:
        dic = {v: k for k, v in enumerate(indices)}
        ret = ''
        for i in range(len(s)):
            ret = ret + s[dic[i]]
        return ret

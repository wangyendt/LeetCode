#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Number of Steps to Reduce a Number in Binary Representation to One
@time: 2020/4/9 14:36
"""


class Solution:
    def numSteps(self, s: str) -> int:
        if len(s) <= 1: return 0

        def add_one(s: str):
            s_list = list(s)
            for i, t in enumerate(s_list[::-1]):
                if t == '0':
                    s_list[~i] = '1'
                    break
                else:
                    s_list[~i] = '0'
            else:
                s_list.insert(0, '1')
            # print(s_list)
            return ''.join(s_list).lstrip('0')

        ret = 1
        while s != '1':
            if s[-1] == '1':
                s = add_one(s)
            else:
                s = s[:-1]
            if s != '1':
                ret += 1
        return ret


so = Solution()
print(so.numSteps('1101'))
print(so.numSteps('10'))
print(so.numSteps('1'))

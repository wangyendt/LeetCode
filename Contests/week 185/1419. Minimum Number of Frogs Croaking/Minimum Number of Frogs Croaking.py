#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/19 11:03
@Author:  wang121ye
@File: Minimum Number of Frogs Croaking.py
@Software: PyCharm
"""

import collections


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnter = collections.Counter()
        res, ret = 0, 0
        for c in croakOfFrogs:
            if c not in 'croak': return -1
            cnter += collections.Counter(c)
            if not cnter['c'] >= cnter['r'] >= cnter['o'] >= cnter['a'] >= cnter['k']: return -1
            # print(cnter)
            if c == 'c':
                res += 1
            elif c == 'k':
                res -= 1
            ret = max(res, ret)
        if not cnter['c'] == cnter['r'] == cnter['o'] == cnter['a'] == cnter['k']: return -1
        return ret


so = Solution()
print(so.minNumberOfFrogs('croakcroak'))
print(so.minNumberOfFrogs('crcoakroak'))
print(so.minNumberOfFrogs('croakcrook'))
print(so.minNumberOfFrogs('croakcroa'))

#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/9 17:00
@Author:  wang121ye
@File: Check If a String Can Break Another String.py
@Software: PyCharm
"""


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1, s2 = sorted(s1), sorted(s2)
        return all([ss1 <= ss2 for ss1, ss2 in zip(s1, s2)]) or all([ss1 >= ss2 for ss1, ss2 in zip(s1, s2)])


so = Solution()
print(so.checkIfCanBreak('abc', 'xya'))
print(so.checkIfCanBreak('abe', 'acd'))
print(so.checkIfCanBreak('leetcode', 'interview'))

#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Repeating Substring
@time: 2020/11/28 22:35
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        idx = 1
        ret = 0
        while word * idx in sequence:
            ret += 1
            idx += 1
        return ret


so = Solution()
print(so.maxRepeating('ababc', 'ab'))

#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Maximum Number of Occurrences of a Substring
@time: 2019/12/24 11:02
"""

import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnter = collections.defaultdict(int)
        for i in range(len(s) - minSize + 1):
            sub_str = s[i:i + minSize]
            if sub_str in cnter or len(set(sub_str)) <= maxLetters:
                cnter[sub_str] += 1
        return max(cnter.values() or [0])


so = Solution()
print(so.maxFreq(s="aababcaab", maxLetters=2, minSize=3, maxSize=4))
print(so.maxFreq(s="aaaa", maxLetters=1, minSize=3, maxSize=3))
print(so.maxFreq(s="aabcabcab", maxLetters=2, minSize=2, maxSize=3))
print(so.maxFreq(s="abcde", maxLetters=2, minSize=3, maxSize=3))

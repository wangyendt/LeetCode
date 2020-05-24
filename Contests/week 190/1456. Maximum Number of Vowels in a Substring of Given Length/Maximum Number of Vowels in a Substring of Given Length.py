#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/24 10:40
@Author:  wang121ye
@File: Maximum Number of Vowels in a Substring of Given Length.py
@Software: PyCharm
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r = 0, k
        cur = 0
        for t in range(l, r):
            if s[t] in 'aeiou':
                cur += 1
        ret = cur
        # print(ret)
        for ll in range(0, len(s) - k):
            if s[ll] in 'aeiou':
                cur -= 1
            if s[ll + k] in 'aeiou':
                cur += 1
            # print(s[ll], s[ll + k], ll, ll + k, cur)
            ret = max(ret, cur)
        return ret


so = Solution()
print(so.maxVowels(s="abciiidef", k=3))
print(so.maxVowels(s="aeiou", k=2))
print(so.maxVowels(s="leetcode", k=3))
print(so.maxVowels(s="rhythms", k=4))
print(so.maxVowels(s="tryhard", k=4))
print(so.maxVowels("weallloveyou", 7))

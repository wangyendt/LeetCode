#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/3/8 2:20
@Author:  wang121ye
@File: Find the Longest Substring Containing Vowels in Even Counts.py
@Software: PyCharm
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d, n, r = {0: -1}, 0, 0
        for i, c in enumerate(s):
            if c in vowels:
                n ^= vowels[c]
            if n not in d:
                d[n] = i
            else:
                r = max(r, i - d[n])
        return r


so = Solution()
print(so.findTheLongestSubstring("eleetminicoworoep"))
print(so.findTheLongestSubstring("leetcodeisgreat"))
print(so.findTheLongestSubstring("bcbcbc"))

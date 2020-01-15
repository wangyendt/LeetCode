#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Distinct Echo Substrings
@time: 2020/1/15 15:47
"""


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        res = set()
        for i in range(len(text)):
            for j in range(i):
                if text[j:i] == text[i:i + i - j]:
                    res.add(text[j:i])
        return len(res)


so = Solution()
print(so.distinctEchoSubstrings(text="abcabcabc"))
print(so.distinctEchoSubstrings(text="leetcodeleetcode"))
print(so.distinctEchoSubstrings(text="aaaaaaaaaaaaa"))

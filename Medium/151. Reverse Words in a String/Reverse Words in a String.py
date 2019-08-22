#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Reverse Words in a String
@time: 2019/8/22 22:46
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed([w for w in s.strip().split(' ') if w]))


so = Solution()
print(so.reverseWords("the sky is blue"))
print(so.reverseWords("  hello world!  "))
print(so.reverseWords("a good   example"))

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/7/11 16:02
# software: PyCharm

from collections import Counter


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[-1 - i]:
                    return False
            return True

        cnt = [(k, v) for k, v in Counter(s).items()]
        cnti = sorted([s.index(c[0]) for c in cnt if c[1] == 1])[::-1]
        n = len(s)
        for ci in cnti:
            if ci >= (n + 1) // 2:
                n = ci

        if not s:
            return ''
        for i in range(n)[::-1]:
            if isPalindrome(s[:i + 1]):
                return s[i + 1:][::-1] + s


so = Solution()
print(so.shortestPalindrome("aacecaaa"), 'aaacecaaa')
print(so.shortestPalindrome("abcd"), 'dcbabcd')
with open('testcase.txt') as f:
    string = f.readlines()[0]
print(so.shortestPalindrome(string))

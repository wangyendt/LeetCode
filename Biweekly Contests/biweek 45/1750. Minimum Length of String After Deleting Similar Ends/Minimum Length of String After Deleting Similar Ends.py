#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Minimum Length of String After Deleting Similar Ends
@time: 2021/02/06 22:44
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1
        while s and s[0] == s[-1]:
            ptr_l = 0
            ls = len(s)
            while ptr_l < ls:
                if s[0] != s[ptr_l]:
                    break
                ptr_l += 1
            if ptr_l == ls:
                return 0
            r = ls - 1
            while r >= ptr_l:
                if s[-1] != s[r]:
                    break
                r -= 1
            s = s[ptr_l:r + 1]
            if len(s) == 1:
                return 1
        return len(s)


so = Solution()
print(so.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))
print(so.minimumLength("abcda"))
print(so.minimumLength("abcba"))
print(so.minimumLength("abccba"))
print(so.minimumLength("aaaaaa"))
print(so.minimumLength("aa"))
print(so.minimumLength("a" * 100001))
print(so.minimumLength("a"))

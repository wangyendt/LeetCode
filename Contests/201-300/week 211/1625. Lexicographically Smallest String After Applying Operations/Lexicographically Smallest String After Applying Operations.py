#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Lexicographically Smallest String After Applying Operations
@time: 2020/10/18 23:52
"""


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        rec = set()

        def dfs(s):
            if s in rec:
                return
            rec.add(s)
            dfs(s[-b:] + s[:-b])
            dfs("".join([str((int(c) + a * (i % 2)) % 10) for i, c in enumerate(s)]))

        dfs(s)
        return min(rec)


so = Solution()
print(so.findLexSmallestString(s="5525", a=9, b=2))

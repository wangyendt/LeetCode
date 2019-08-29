#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Remove Invalid Parentheses
@time: 2019/8/29 17:40
"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> list:
        s = s[s.find('('):s.rfind(')') + 1]
        if not s: return []
        n1, n2 = sum([1 for ss in s if ss == '(']), sum([1 for ss in s if ss == ')'])
        print(n1, n2)

        def dfs(path):
            pass


so = Solution()
print(so.removeInvalidParentheses('a((sdfas'))

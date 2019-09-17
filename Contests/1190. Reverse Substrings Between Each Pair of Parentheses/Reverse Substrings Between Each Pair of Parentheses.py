#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Reverse Substrings Between Each Pair of Parentheses
@time: 2019/9/17 15:04
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for ss in s:
            if ss not in '()':
                stack[-1] += ss
            elif ss == '(':
                stack.append('')
            elif ss == ')':
                sss = stack.pop()
                stack[-1] += sss[::-1]
        return stack[-1]


so = Solution()
print(so.reverseParentheses("(abcd)"))
print(so.reverseParentheses("(u(love)i)"))
print(so.reverseParentheses("(ed(et(oc))el)"))
print(so.reverseParentheses("a(bcdefghijkl(mno)p)q"))

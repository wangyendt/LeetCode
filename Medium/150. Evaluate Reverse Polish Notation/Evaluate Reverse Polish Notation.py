#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Evaluate Reverse Polish Notation
@time: 2019/8/22 22:37
"""


class Solution:
    def evalRPN(self, tokens: list) -> int:
        digit_stack = []
        for t in tokens:
            if t in '+-*/':
                p, q = digit_stack.pop(), digit_stack.pop()
                digit_stack.append(int(eval('q' + t + 'p')))
            else:
                digit_stack.append(int(t))
        return digit_stack[-1]


so = Solution()
print(int(4/3),int(-4/3))
print(so.evalRPN(["2", "1", "+", "3", "*"]))

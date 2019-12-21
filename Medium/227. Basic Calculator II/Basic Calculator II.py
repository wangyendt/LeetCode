#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Basic Calculator II.py 
@time: 2019/12/21
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        if not s: return 0
        stack, res, sign = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
            if not s[i].isdigit() or i == len(s) - 1:
                if sign == '+':
                    stack.append(res)
                elif sign == '-':
                    stack.append(-res)
                elif sign == '*':
                    stack.append(stack.pop() * res)
                elif sign == '/':
                    tmp = stack.pop()
                    if tmp // res < 0 and tmp % res != 0:
                        stack.append(tmp // res + 1)
                    else:
                        stack.append(tmp // res)
                sign = s[i]
                res = 0
        return sum(stack)


so = Solution()
print(so.calculate("3+2*2"))
print(so.calculate(" 3/2 "))

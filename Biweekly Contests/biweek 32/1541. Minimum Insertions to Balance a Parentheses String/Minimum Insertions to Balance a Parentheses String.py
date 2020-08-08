#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: Minimum Insertions to Balance a Parentheses String.py 
@time: 2020/08/09
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        res = right = 0
        for c in s:
            if c == '(':
                if right % 2:
                    right -= 1
                    res += 1
                right += 2
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return right + res


so = Solution()
# print(so.minInsertions(s="(()))"))
# print(so.minInsertions(s="())"))
# print(so.minInsertions(s="))())("))
# print(so.minInsertions(s="(((((("))
# print(so.minInsertions(s=")))))))"))
# print(so.minInsertions("()()()()()("))
print(so.minInsertions("(()))(()))()())))"))

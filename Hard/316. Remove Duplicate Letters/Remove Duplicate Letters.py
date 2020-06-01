#!/usr/bin/env python
# encoding: utf-8

"""
@author: Wayne
@contact: wangye.hope@gmail.com
@software: PyCharm
@file: Remove Duplicate Letters
@time: 2020/06/01 14:58
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_ind = {v: i for i, v in enumerate(s)}
        stack = []
        for i in range(len(s)):
            # print(stack, i, s[i])
            if s[i] in stack: continue
            while stack and stack[-1] > s[i] and i < last_ind[stack[-1]]:
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)



so = Solution()
print(so.removeDuplicateLetters('bcabc'))
print(so.removeDuplicateLetters('cbacdcbc'))

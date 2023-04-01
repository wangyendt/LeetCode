# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wang121ye
# datetime: 2019/9/29 12:15
# software: PyCharm
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ss in s:
            if not stack:
                stack.append([ss,1])
            else:
                if ss == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([ss,1])
            if stack[-1][1] == k:
                stack.pop()
        return ''.join([k[0]*k[1] for k in stack])

so  =Solution()
print(so.removeDuplicates(s = "abcd", k = 2))
print(so.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
print(so.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))
